import pandas as pd
import os

def fetch_excel(file):
    folder_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(folder_path,'Data')
    file_path = os.path.join(data_path, file)
    
    df = pd.read_excel(file_path)
    rows = df.values.tolist()
   
    return rows
    
