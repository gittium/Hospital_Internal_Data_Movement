from Extract.extract_csv import fetch_csv
from Extract.extract_excel import fetch_excel
from Extract.extract_postgres import extract_postgres
from Extract.extract_api import fetch_api
import pandas as pd

int_field = [ 'id' , 'contact']
string_field = ['hospital_name' , 'hostpital_branch' , 'patient_name']
def validate_field_type(row):

   
    for key in row :
        if key in int_field:
            if not isinstance (row[key] , int ):
                raise ValueError(f"invalid type {row[key]} is not int")
           
            
        elif key in string_field:
            if not isinstance (row[key] , str):
                raise ValueError(f"invalide type {row[key]} is not string" )
    return print("valid type of data")
        
        
        
        
    
def validate_empty(row):
    
    for key in row:
        if not str(row[key]).strip():
            raise ValueError("got empty data")
        
    return print("data not empty")
        
    
    
def validate_num_rows(row):
    fields = ['id' , 'hospital_name' , 'hospital_branch' , 'contact' , 'patient_name' ]
    if len(row) != len(fields):
        raise ValueError(f"schema validation failed, exptected {len(fields)} rows got {len(row)}: {row} " )
    

# rows , head = fetch_csv('hospital_data.csv')
# list_row = [dict(zip(head,row)) for row in rows ]

# for row in list_row:
#     for ket in row:
#         print(ket)
  
# list = fetch_api('http://127.0.0.1:8000/mock-patient')
# print(list)
# for row in list:
#     validate_num_rows(row)
        

# validate_field_type(list)
# validate_empty(list)