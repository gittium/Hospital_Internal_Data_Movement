import pandas as pd
import os

def fetch_excel(file):
    folder_path = os.path.dirname(os.path.abspath(__file__))
    more_folder = os.path.dirname(folder_path)
    print(more_folder)
    data_path = os.path.join(more_folder,'Data')
    print(data_path)
    file_path = os.path.join(data_path , file )
   

   
    df = pd.read_excel(file_path)
    
    datetime_header = ['วันเกิด' , 'วันที่เข้ารักษา'  , 'วันที่จำหน่าย']
    
    for head in datetime_header:
        df[head] = pd.to_datetime(df[head])
        print(df[head].dtypes)
        
    header = df.columns.tolist()
    
    
    rows = df.values.tolist()
   
    return rows  , header

rows , header = fetch_excel('mock_patient.xlsx')
print(rows)

print(header)