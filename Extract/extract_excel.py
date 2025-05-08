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
    header = df.columns.tolist()
   
    
    rows = df.values.tolist()
   
    return rows  , header

