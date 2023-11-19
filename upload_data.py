import os

from azure.data.tables import TableServiceClient
from dotenv import  load_dotenv

PRODUCT_NAME = u'ELFS'


byrne_elfs = [
    {
        u'PartitionKey': PRODUCT_NAME,
        u'ElfName': "Tinsel Twinkle-Toes",
        u'RowKey': "Tara",
        u'Password': "Elf_pi",
        u'Assigned': "False"
    },
    {
    u'PartitionKey': PRODUCT_NAME,
    u'ElfName': "Lorcan Twinklesprout",
    u'RowKey': "Louis",
    u'Password': "Elf_li",
    u'Assigned': "False"
    },
    {
        u'PartitionKey': PRODUCT_NAME,
        u'ElfName': "Pixie Pointy-Ears",
        u'RowKey': "Kyra",
        u'Password': "Elf_ki",
        u'Assigned': "False"
    },
    {
    u'PartitionKey': PRODUCT_NAME,
    u'ElfName': "Maura Merrywhistle",
    u'RowKey': "Maureen",
    u'Password': "Elf_ti",
    u'Assigned': "False"
    },
    {
    u'PartitionKey': PRODUCT_NAME,
    u'ElfName': "Molly Merrybottom",
    u'RowKey': "Mirjam",
    u'Password': "Elf_si",
    u'Assigned': "False"
    }
]

if __name__ == '__main__':
    print("DO NOT USE")
    load_dotenv()
    table_service_client = \
        TableServiceClient.from_connection_string(conn_str=os.getenv("CONN_STR"))
    table_client = table_service_client.get_table_client(table_name="byrneElfs")
    for elf in byrne_elfs:
        table_client.create_entity(entity=elf)
