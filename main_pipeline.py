from leanbasic.ETL.Extract.extract_postgres import extract_data 
from tranform import tranform_data 
from load import load_data
from leanbasic.ETL.Extract.extract_csv import fetch_csv
from leanbasic.ETL.Extract.extract_excel import fetch_excel
from leanbasic.ETL.Extract.extract_api import fetch_api
from error_handling import validate_field_type, validate_empty , validate_num_rows
from hash_data import final_hashed
from leanbasic.ETL.Dynamic_Table.scan_schema import scan_table
import psycopg2
from connect import connection


conn = connection()

def run_etl():
    
    print("which data type")
    print("1.csv")
    print("2.excel")
    print("3.postgres")
    # raw_data = extract_data()
    
    
    
    option = input("enter number: ")
    
    match option:
        case "1" :
            raw_data = fetch_csv()
        case "2" : 
            raw_data = fetch_excel()
        case "3" :
            raw_data = extract_data()
        case _:
            print("not supported")
            
    print("extract_module_success")
    
    


    
    mask_field = ['patient_name']    
  
    
    cleaned_row = []
    
    try:    
        for i , row in enumerate(raw_data):
            validate_num_rows(row)
            validate_field_type(row)
            validate_empty(row)
            
            print("validate raw data success")
            
            cleaned_data = tranform_data(row)
            cleaned_data = final_hashed(cleaned_data ,mask_field ,salt = "nuhospital"  )
            print("hashed success")
            cleaned_row.append(cleaned_data)
            print("clean_module_success")
    except Exception as e :
        print(f"row{i}" ,e )
    
    
    
    
    load_data(cleaned_row)
    print("load_module_sucess")
    
if __name__=="__main__":
    run_etl()
        
    
    