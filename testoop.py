
from Extract.oopsql import ExtractSQL
from sqlalchemy import create_engine
from Pipeline.viewtable import ShowTableColumn , ShowFK
from tranform import Tranform
from Dynamic_Table.gen_sql_table import GenTable

# print(ExtractAPI('http://127.0.0.1:8000/mock-patient').extract())

engine = create_engine("postgresql+psycopg2://postgres:admin@localhost:5432/postgres")
table_name = ['patient']
masking = ['ชื่อนามสกุล','รหัสบัตรประชาชน' ,'เลขกรมธรรม์']



# [dict(zip(header, row)) for row in raw_data]


# Tranform().tranform_data()


# ShowTable(engine)
# ShowFK(engine , table_name)
# list = (ShowTableColumn(engine).show())



# ShowFK(engine , table_name)


rows , header  = ExtractSQL(engine , table_name).extract()
new_table = "test patient"
list = [dict(zip(header, row)) for row in rows]
tranforms = []
for data_row in list:
   tranforms.append(Tranform(data_row , masking).tranform_data())

# print(tranforms)
    
query = GenTable(new_table , tranforms ).gen_sql_table()
print(query)
    