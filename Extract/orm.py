from sqlalchemy import inspect , create_engine ,MetaData , inspect
# from Extract.rule_extract import RuleExtract


# class ExtractDB(RuleExtract):
    
#     def __init__(self , uri_db , column_name):
#         self.db = uri_db
#         self.column_name = column_name
        
#     def extract(self):
#         engine = create_engine(self.db)
        
        
        
        



    
    

engine = create_engine("postgresql+psycopg2://postgres:admin@localhost:5432/postgres")


inspector = inspect(engine)

columns = inspector.get_columns('patient')
metadata = MetaData()
metadata.reflect(bind=engine)




fks = inspector.get_foreign_keys("patient")
if (fks[0]['referred_schema']) == None :
    print("no schema")



# for Column in metadata.inspect:
#     print(f"{Column}")

# column_names = ['patient_id', 'full_name', 'birth_date', 'gender', 'diagnosis']


# column_input 