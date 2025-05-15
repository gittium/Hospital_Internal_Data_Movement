from Extract.rule_extract import RuleExtract
from Extract.connect import connection
import psycopg2

conn = connection()

class ExtractPosgres(RuleExtract):
    
    def __init__(self , table_name , conn):
        self.table_name = table_name
        self.conn = conn
        
        
    def extract(self):
        
        cur = conn.cursor()
        
        query  = f"SELECT * FROM {self.table_name} ;"
        
        cur.execute(query)
        
        raw_rows = cur.fetchall()
        
        rows = []
        for row in raw_rows:
            row = list(row)
            rows.append(row)
            
        
        
        query = "SELECT column_name from information_schema.columns WHERE table_name = %s"
        
        
        cur.execute(query , (self.table_name,))
        
        head_data = cur.fetchall()
        
        # listdict = ([dict(zip(head , row)) for row in rows ])
        
        header = []
        
        for row in head_data:
            for i  in row:
                header.append(i)
            
        return rows , header
            
        
        