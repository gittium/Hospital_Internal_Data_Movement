from Extract.extract_postgres import extract_postgres 

from load import load_data
from Extract.extract_csv import fetch_csv
from Extract.extract_excel import fetch_excel
from Extract.extract_api import fetch_api
from error_handling import validate_field_type, validate_empty , validate_num_rows
from hash_data import  final_hashed2 , final_hashed3

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
            file = input("enter file name: ")
            raw_data , header = fetch_csv(file)
            raw_data = [dict(zip(header, row)) for row in raw_data]
            print(f"raw_data_before{raw_data}")
            print(f"raw_header_before{header}")
        case "2" : 
            file = input("enter file name: ")
            raw_data , header = fetch_excel(file)
            raw_data = [dict(zip(header, row)) for row in raw_data]
        case "3" :
            table_name = input("Enter Source Table Name: ")
            raw_data , header = extract_postgres(table_name)
            raw_data = [dict(zip(header, row)) for row in raw_data]
        case "4" :
            source_api = input("enter API URL: ")
            raw_data , header = fetch_api(source_api)
            print(f"raw_data_before{raw_data}")
            print(f"raw_header_before{header}")
        case _:
            print("not supported")
            
    print("extract_module_success")
  
    


    
    mask_field = ['patient_name']    
  
    
    
    hashed_rows = []
    try:    
        for i , row in enumerate(raw_data):
            # validate_num_rows(row)
            validate_empty(row)
            validate_field_type(row)
            validate_num_rows(row)
            
            print("validate raw data success")
            
            
            # print("start tranform")
            # cleaned_data = tranform_data(row)   #cleaned_data is a dict
            # print("tranform success")
            print( "start hash")
            hash_row = final_hashed3(row , mask_field , salt = "hostpital")
            hashed_rows.append(hash_row)
            print( "hash_success")
            
   
    except Exception as e :
        print(f"row{i}" ,e )
        
    print(hashed_rows)
    
    new_table_name = input("Enter Destination Table Name: ")
    new_create_table = create_table(hashed_rows , new_table_name , conn , header)
    print(new_create_table)
    cur = conn.cursor()
    cur.execute(new_create_table)
    conn.commit()
    
    
    
    
    load_data(hashed_rows, new_table_name , conn)
    print("load_module_sucess")
    
if __name__=="__main__":
    run_etl()
    