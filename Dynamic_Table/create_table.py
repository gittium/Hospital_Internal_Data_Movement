# from scan_schema import scan_table
from Dynamic_Table.gen_sql_table import gen_sql_table
from Dynamic_Table.scan_python_schema import scan_python_schema


def create_table(cleaned_data , new_table , conn , headers):
   
    
    
    schema = scan_python_schema(cleaned_data , headers)
    table = gen_sql_table(new_table, schema)
    
    
    cur = conn.cursor()
    
    cur.execute(table)
    return table
    
    
    
    
    
    

    
    
    

    
    
    
    
    
   
    
    