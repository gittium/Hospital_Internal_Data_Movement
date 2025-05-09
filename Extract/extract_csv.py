import csv
import os
import pandas as pd

def fetch_csv(file):
    
    folder_path = os.path.dirname(os.path.abspath(__file__))
    before_data_path = os.path.dirname(folder_path)
    data_path = os.path.join(before_data_path,'Data')
    file_path = os.path.join(data_path,file)
    print(file_path)
    
    
    df = pd.read_csv(file_path)
    header = df.columns.tolist()
   
    
    rows = df.values.tolist()
   
    return rows  , header
    
    # csv_row = []
    
    
    
    
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







    
