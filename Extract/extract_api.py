import requests

def fetch_api(url):
    # create variable to get api
    
    response = requests.get(url)
    print("Status code:", response.status_code)  
    
    
    if response.status_code == 200 :
        data = response.json()
        first = data[0]
        header = first.keys()
        return data , list(header)
        
        
        
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


        