
from Extract.oopsql import ExtractSQL
from sqlalchemy import create_engine
from Pipeline.viewtable import ShowTableColumn , ShowFK


# print(ExtractAPI('http://127.0.0.1:8000/mock-patient').extract())

engine = create_engine("postgresql+psycopg2://postgres:admin@localhost:5432/postgres")
table_name = ['patient']



# ShowTable(engine)
# ShowFK(engine , table_name)
# ShowTableColumn(engine)

# ShowFK(engine , table_name)


ExtractSQL(engine , table_name).extract()