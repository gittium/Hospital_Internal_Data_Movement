from Extract.rule_extract import RuleExtract
import os
import pandas as pd

class ExtractExcel(RuleExtract):
    
    def __init__ (self ,file):
        self.file = file
        self.datetime =  ['วันเกิด' , 'วันที่เข้ารักษา'  , 'วันที่จำหน่าย']
        
        
    def extract(self):
        folder_path = os.path.dirname(os.path.abspath(__file__))
        more_folder = os.path.dirname(folder_path)
        
        data_path = os.path.join(more_folder,'Data')
       
        file_path = os.path.join(data_path , self.file )
        
        df = pd.read_excel(file_path)
        
        for date in self.datetime:
            df[date] = pd.to_datetime(df[date])
        
        header = df.columns.tolist()
        rows = df.values.tolist()
        
        return rows , header
        
    
    