import csv
import os

def fetch_csv(file_path):
    
    folder_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(folder_path,'Data')
    file_path = os.path.join(data_path,file_path)
    print(file_path)
    
    csv_row = []
    
    
    
    
    with open(file_path , newline='' , encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)   # skipp first row that's header
        
        for row in reader:
            csv_row.append(row)
            
    return csv_row



    
