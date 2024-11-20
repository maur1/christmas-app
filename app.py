import streamlit as st
from dotenv import load_dotenv
from azure.data.tables import TableClient
import os
import time as time
from azure_data import get_elf_name, get_list_of_unassinged_elfs, update_elf_assignment, update_elf_picked, \
    has_elf_picked, get_assigned_elf
import random


load_dotenv()
# SET_UP
PRODUCT_NAME = u'ELFS'
table_client = TableClient.from_connection_string(conn_str=os.getenv("CONN_STR"), table_name=os.getenv("ELF_TABLE"))

my_bar = st.progress(0)

family_names = ["Louis", "Mirjam", "Tara", "Kyra", "Maureen"]

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
# Add a title and intro text
st.title("🎅 The Byrne Elfs Christmas 🎅")
st.write("Start by entering your name")
real_name = st.text_input(
    "Enter yor real name 👨",
    label_visibility=st.session_state.visibility,
    disabled=st.session_state.disabled,
    placeholder="Roger",
)

if real_name:
    if real_name not in family_names:
        st.error(f"Invalid name, must be one of {family_names}")
    else:
        st.write("You entered: ", real_name)
        my_bar.progress(50)
        st.write("Your Elf name is:")
        elf_name= get_elf_name(real_name, table_client)
        st.write(f"🧝 {elf_name} 🧝")

        if has_elf_picked(table_client, real_name):
            st.error("🦖🦖🦖You have already picked an Elf 🦖🦖🦖")
            st.error("contact Maureen to retrieve your special elf password and enter it here:")
            password_in = st.text_input(
                "✨ Enter special elf password ✨",
                label_visibility=st.session_state.visibility,
                disabled=st.session_state.disabled,
                placeholder="password123",
                type="password"
            )
            assigned_elf = get_assigned_elf(name=real_name, password=password_in, table_client=table_client)
            if assigned_elf:
                st.write("Your assigned elf is 🧝")
                st.write(f"🧝 {assigned_elf} 🧝")
            else:
                st.error("🦖🦖🦖Incorrect password🦖🦖🦖")
        else:
            with st.spinner('Santa is finding an Elf for you 🎅 hoho'):
                st.snow()
                time.sleep(5)

            unassigned_elfs = get_list_of_unassinged_elfs(table_client, real_name)
            if not unassigned_elfs:
                st.error("No more Elfs left, contact Maureen for info")
            else:
                assigned_elf = random.choice(unassigned_elfs)
                update_elf_assignment(assigned_elf, table_client)
                update_elf_picked(real_name, assigned_elf, table_client)
                st.write(f"Your have to find a gift for Elf friend")
                st.subheader(f"🧝‍♀ {assigned_elf} 🧝‍")
                st.snow()
