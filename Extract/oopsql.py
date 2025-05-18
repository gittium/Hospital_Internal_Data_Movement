from Extract.rule_extract import RuleExtract
from sqlalchemy import table , select , create_engine , inspect , MetaData
from Pipeline.viewtable import ShowTableColumn


class ExtractSQL(RuleExtract):
    
    def __init__(self  , engine, table_name):
        self.table_name = table_name
        self.engine = engine
        
        
    def extract(self):
        
        
        
        metadata = MetaData()
        metadata.reflect(bind=self.engine)
        
        all_table_name = []
        for table in self.table_name:
            table = metadata.tables[table] 
            
            stmt = select(table)
            
            with self.engine.connect() as conn:
                result = conn.execute(stmt).fetchall()
                list_rows = [list(row) for row in result]
                print(list_rows)
                
        
        header = ShowTableColumn(self.engine).show()
        
        return list_rows , header           
                    
            
           
        
            
            
        
        
        
        
     



        
        
        
        
        
        # cur = conn.cursor()
        
        # query  = f"SELECT * FROM {self.table_name} ;"
        
        # cur.execute(query)
        
        # raw_rows = cur.fetchall()
        
        # rows = []
        # for row in raw_rows:
        #     row = list(row)
        #     rows.append(row)
            
        
        
        # query = "SELECT column_name from information_schema.columns WHERE table_name = %s"
        
        
        # cur.execute(query , (self.table_name,))
        
        # head_data = cur.fetchall()
        
        # # listdict = ([dict(zip(head , row)) for row in rows ])
        
        # header = []
        
        # for row in head_data:
        #     for i  in row:
        #         header.append(i)
            
        # return rows , header
            
        
        