import os
from dotenv import load_dotenv
from azure.data.tables import TableClient
import random

PRODUCT_NAME = u'ELFS'

def get_list_of_unassinged_elfs(table_client, elf_asking: str):
    my_filter = "Assigned eq @assigned"
    params = {"assigned": "False"}
    entities = table_client.query_entities(query_filter=my_filter, select=["RowKey"], parameters=params)
    if entities:
        not_chosen = [list(entity.values())[0] for entity in entities]
        if elf_asking in not_chosen:
            not_chosen.remove(elf_asking)
    else:
        not_chosen = None
    random.shuffle(not_chosen)
    return not_chosen


def has_elf_picked(table_client, elf_asking: str):
    my_filter = "Picked eq @picked"
    params = {"picked": "True"}
    entities = table_client.query_entities(query_filter=my_filter, select=["RowKey"], parameters=params)
    elf_w_assignments = [list(entity.values())[0] for entity in entities]
    return elf_asking in elf_w_assignments


def update_elf_assignment(chosen_name: str, table_client: TableClient):
    entity = {
        u'PartitionKey': PRODUCT_NAME,
        u'RowKey': chosen_name,
        u'Assigned': "True"
    }
    print(table_client.update_entity(entity=entity))


def update_elf_picked(elf_asking: str, assigned_elf: str, table_client: TableClient):
    entity = {
        u'PartitionKey': PRODUCT_NAME,
        u'RowKey': elf_asking,
        u'Picked': "True",
        u'AssignedElf': assigned_elf
    }
    print(table_client.update_entity(entity=entity))


def get_elf_name(name: str, table_client: TableClient) -> str:
    entities = table_client.get_entity(partition_key="ELFS", row_key=name)
    return entities["ElfName"]

def get_assigned_elf(name: str, password: str,table_client: TableClient) -> str:
    entities = table_client.get_entity(partition_key="ELFS", row_key=name)
    print(entities)
    if entities["Password"] == password:
        return entities["AssignedElf"]
    return None

if __name__ == '__main__':
    load_dotenv()
    table_client = TableClient.from_connection_string(conn_str=os.getenv("CONN_STR"), table_name="byrneElfs")
    my_filter = "Assigned eq @assigned"
    params = {"assigned": "False"}
    entities = table_client.query_entities(query_filter=my_filter, select=["RowKey"], parameters=params)
    elf_w_assignments = [list(entity.values())[0] for entity in entities]
    print(elf_w_assignments)
