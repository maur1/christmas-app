import os

from azure.data.tables import TableServiceClient
from datetime import datetime
from dotenv import  load_dotenv

PRODUCT_NAME = u'ELFS'


byrne_elfs = [{
    u'PartitionKey': PRODUCT_NAME,
    u'ElfName': Snickerdoodle,
    u'RowKey': "Louis",
    u'Assigned': "False"
},{
    u'PartitionKey': PRODUCT_NAME,
    u'ElfName': "Elfi McElfFace",
    u'RowKey': "Maureen",
    u'Assigned': "False"
},{
    u'PartitionKey': PRODUCT_NAME,
    u'ElfName': "Molly Merrybottom",
    u'RowKey': "Mirjam",
    u'Assigned': "False"
}
,{
    u'PartitionKey': PRODUCT_NAME,
    u'ElfName': "Pixie Pointy-Ears",
    u'RowKey': "Kyra",
    u'Assigned': "False"
}, {
    u'PartitionKey': PRODUCT_NAME,
    u'ElfName': "Tinsel Twinkle-Toes",
    u'RowKey': "Tara",
    u'Assigned': "False"
}]

if __name__ == '__main__':
    load_dotenv()
    table_service_client = \
        TableServiceClient.from_connection_string(conn_str=os.getenv("CONN_STR"))
    table_client = table_service_client.get_table_client(table_name="byrneElfs")
    for elf in byrne_elfs:
        table_client.create_entity(entity=elf)
