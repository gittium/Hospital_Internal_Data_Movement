import requests

def fetch_api(url):
    # create variable to get api
    
    response = requests.get(url)
    print("Status code:", response.status_code)  
    
    
    if response.status_code == 200 :
        data = response.json()
        
        # fields = list(data[0].keys())
        # print(fields)
        fields = ["hospital_name", "hostpital_branch", "address", "contact"]

        
        
        raw_data = []
        
        for dict in data:
            values=[]
            for field in fields :
                value = dict.get(field)
                values.append(value)
            raw_data.append(values)
            
        for row in raw_data:
            print(row)
        return raw_data
    
    else :
        print("cant fetch api")
            

fetch_api('https://run.mocky.io/v3/06d36077-1335-44b1-84d1-b9d04d1d4d22')


        