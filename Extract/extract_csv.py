import csv
import os
import pandas as pd
from datetime import datetime

def fetch_csv(file):
    
    folder_path = os.path.dirname(os.path.abspath(__file__))
    before_data_path = os.path.dirname(folder_path)
    data_path = os.path.join(before_data_path,'Data')
    file_path = os.path.join(data_path,file)
    print(file_path)
    
    
    df = pd.read_csv(file_path , encoding='utf-8-sig')
    
    datetime_header = ['วันเกิด' , 'วันที่เข้ารักษา'  , 'วันที่จำหน่าย']
    
    for head in datetime_header:
        df[head] = pd.to_datetime(df[head])
        
        
    header = df.columns.tolist()
    
    
    
    rows = df.values.tolist()
    return rows , header
    
    
   
rows , header = fetch_csv('mock_patient.csv')   
print(rows)
print(header)
    # csv_row = []
    


# head = rows.columns.tolist()



# print(rows['วันที่เข้ารักษา'].head(10))
# date = rows[0][3]
# print(date)
# print(isinstance(date , datetime))
    
    
    # with open(file_path , newline='' , encoding='utf-8') as file:
    #     reader = csv.reader(file)
    #     list_csv = list(reader)   
     
        
    #     for row in list_csv:
    #         if list_csv.index(row) ==0:
    #             continue
    #         csv_row.append(row)
            
    # return csv_row , list_csv[0]



# print(row)
# for i in row:
    
#     for j in i:
        
#         print(j)
#     break
         
# print(head)







    
