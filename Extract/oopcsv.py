from Extract.rule_extract import RuleExtract
import os 
import pandas as pd


        

class ExtractCsv(RuleExtract):
    
    def __init__(self , file):
        
        self.file = file
        self.datetime_header = ['วันเกิด' , 'วันที่เข้ารักษา'  , 'วันที่จำหน่าย']
        
    def extract(self):  #override
        folder_path = os.path.dirname(os.path.abspath(__file__))
        before_data_path = os.path.dirname(folder_path)
        data_path = os.path.join(before_data_path,'Data')
        file_path = os.path.join(data_path, self.file)
        
        df = pd.read_csv(file_path , encoding='utf-8-sig')
        
        for date in self.datetime_header:
            df[date] = pd.to_datetime(df[date])
        
        header = df.columns.tolist()
        rows = df.values.tolist()
        
        return rows , header
        
        
        
        
        
# extract = (ExtractCsv('mock_patient.csv'))   #object extractcsv




    
   