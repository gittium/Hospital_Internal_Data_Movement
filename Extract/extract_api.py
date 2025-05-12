import requests
import pandas as pd

def fetch_api(url):
    # create variable to get api
    
    response = requests.get(url)
    print("Status code:", response.status_code)  
    
    
    if response.status_code == 200 :
        
        data = response.content.decode('utf-8-sig')
        data = response.json()
        df = pd.DataFrame(data)
        
        print(df.columns.tolist())
        datetime = ['วันเกิด' , 'วันที่เข้ารักษา' , 'วันที่จำหน่าย']
        
        for date in datetime:
            df[date] = pd.to_datetime(df[date])
            
        
        
        
        header = df.columns.tolist()
        rows = df.values.tolist()
        return rows , list(header)
        
        
        
rows , header = fetch_api('http://127.0.0.1:8000/mock-patient')
print(rows)
print(header)

        # fields = list(data[0].keys())
        # print(fields)
    #     fields = ["hospital_name", "hostpital_branch", "contact" , "patient_name"]

        
        
    #     raw_data = []
        
    #     for dict in data:
    #         values=[]
    #         for field in fields :
    #             value = dict.get(field)
    #             values.append(value)
    #         raw_data.append(values)
            
    #     for row in raw_data:
    #         print(row)
    #     return raw_data
    
    # else :
    #     print("cant fetch api")
            
# api , head = fetch_api('http://127.0.0.1:8000/mock-patient')
# print(api)
# print(head)


        