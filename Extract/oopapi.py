from Extract.rule_extract import RuleExtract
import requests
import pandas as pd

class ExtractAPI(RuleExtract):
    
    def __init__(self , api):
        self.api = api
        self.datetime = ['วันเกิด' , 'วันที่เข้ารักษา'  , 'วันที่จำหน่าย']
        
        
    def extract(self):
        
        response = requests.get(self.api)
        
        if response.status_code == 200 :
            data = response.json()
            header = []
            rows = []
            for dict in data:
               
                for key in dict:
                    if key in self.datetime:
                        dict[key] = pd.to_datetime(dict[key])
                rows.append(list(dict.values()))
            
            for char in data[0]:
                 header.append(char)
                                    
        return rows , header
        
                    
            
           
               
                
                
                

            
        
        
        
        
        
        