from sqlalchemy import inspect , MetaData
from Extract import oopsql

class ShowTableColumn:
    
    def __init__(self , engine):
        self.engine = engine




        
        
         # will use in extract
         
    def show(self):
        inspector = inspect(self.engine)
        
        
        tables = inspector.get_table_names()
        
        
        for i , col in enumerate(tables):
            
            column = inspector.get_columns(col)
            
            column_name = [(dict['name']) for dict in column]
        return column_name
            



        
        
class ShowFK:
    def __init__(self , engine, table_name):
        self.engine = engine
        self.table_name = table_name
        
        inspector = inspect(self.engine)
        
        for table in self.table_name:
            fk_table =  inspector.get_foreign_keys(table)
            
            if fk_table:
                print(f" __{table}__ have relationship with table __{fk_table[0]['referred_table']}__ Do you still want to Proceed?")
                
            else:
                continue