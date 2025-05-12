from Extract.extract_csv import fetch_csv
from Extract.extract_excel import fetch_excel
from Extract.extract_postgres import extract_postgres
from Extract.extract_api import fetch_api
import pandas as pd
from datetime import date , datetime


datetime_field = ['วันเกิด' , 'วันที่เข้ารักษา' , 'วันที่จำหน่าย']
string_field = ['รหัสผู้ป่วย' , 'ชื่อนามสกุล' ,'รหัสบัตรประชาชน', 'วันเกิด', 'เพศ', 'เบอร์โทรศัพท์', 'อีเมล', 'ที่อยู่', 'โรคประจำตัว', 'เลขกรมธรรม์']
def validate_field_type(row):

   
    for key in row :
        if key in datetime_field:
            if not isinstance (row[key] , (pd.Timestamp , datetime , date)):
                raise ValueError(f"invalid type {row[key]} is not datetime")
           
            
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
    fields = ['รหัสผู้ป่วย', 'ชื่อนามสกุล', 'รหัสบัตรประชาชน', 'วันเกิด', 'เพศ', 'เบอร์โทรศัพท์', 'อีเมล', 'ที่อยู่', 'โรคประจำตัว', 'เลขกรมธรรม์', 'วันที่เข้ารักษา', 'วันที่จำหน่าย' ]
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
rows , header = extract_postgres('hospital')

zip_list = [dict(zip(header , row)) for row in rows]
for row in zip_list:
    validate_field_type(row)
    validate_num_rows(row)
    validate_empty(row)