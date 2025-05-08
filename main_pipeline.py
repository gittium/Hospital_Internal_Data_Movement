from Extract.extract_postgres import extract_postgres 

from load import load_data
from Extract.extract_csv import fetch_csv
from Extract.extract_excel import fetch_excel
from Extract.extract_api import fetch_api
from error_handling import validate_field_type, validate_empty 
from hash_data import  final_hashed2

import psycopg2
from connect import connection


from Dynamic_Table.create_table import create_table


conn = connection()
        
    
def run_etl():
    
    print("which data type")
    print("1.csv")
    print("2.excel")
    print("3.postgres")
    print("4.api")
    # raw_data = extract_data()
    
    
    
    option = input("enter number: ")
    
    match option:
        case "1" :
            raw_data , header = fetch_csv('dummy_data.csv')
        case "2" : 
            raw_data , header = fetch_excel('dummy_data.xlsx')
        case "3" :
            table_name = input("Enter Table Name: ")
            raw_data , header = extract_postgres(table_name)
        case "4" :
            raw_data = fetch_api('http://127.0.0.1:8000/mock-patient')
        case _:
            print("not supported")
            
    print("extract_module_success")
  
    


    
    mask_field = ['patient_name']    
  
    
    
  
    try:    
        for i , row in enumerate(raw_data):
            # validate_num_rows(row)
            # validate_field_type(row)
            # validate_empty(row)
            
            print("validate raw data success")
            
            cleaned_data = [dict(zip(header, row)) for row in raw_data]
            # print("start tranform")
            # cleaned_data = tranform_data(row)   #cleaned_data is a dict
            # print("tranform success")
            print( "start hash")
            hashed_data = final_hashed2(cleaned_data ,mask_field ,salt = "nuhospital"  )
            print("hashed success")
            print(hashed_data)
            print("clean_module_success")
    except Exception as e :
        print(f"row{i}" ,e )
        
    
    
    new_table_name = input("Enter Destination Table Name: ")
    new_create_table = create_table(cleaned_data , new_table_name , conn , header)
    
    cur = conn.cursor()
    cur.execute(new_create_table)
    conn.commit()
    
    
    
    
    load_data(cleaned_data, new_table_name , conn)
    print("load_module_sucess")
    
if __name__=="__main__":
    run_etl()
    