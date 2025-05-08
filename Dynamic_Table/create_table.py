# from scan_schema import scan_table
from Dynamic_Table.gen_sql_table import gen_sql_table
from Dynamic_Table.scan_python_schema import scan_python_schema
from Dynamic_Table.connect import connection



conn = connection()


def create_table(cleaned_data , new_table_name , conn , headers):
   
    
    
    schema = scan_python_schema(cleaned_data , headers)
    table = gen_sql_table(new_table_name, schema)
    
    
    cur = conn.cursor()
    
    cur.execute(table)
    return table
    
    
# cleaned_data = fetch_api('http://127.0.0.1:8000/mock-patient')
# headers = ["hospital_name", "hostpital_branch", "contact", "patient_name"]

# print(create_table(cleaned_data , 'test_api_hos' , conn , headers))



    

    
    
    

    
    
    
    
    
   
    
    