

import pandas as pd

def gen_sql_table(new_table_name , hashed):
    columns = []
    
    first_dict = hashed[0]
    list_column = list(first_dict.keys())
    
    for  i , key  in enumerate(first_dict):
        
        column_name = list_column[i]
        
        if isinstance(first_dict[key], (pd.Timestamp)):
            column_type = 'TIMESTAMP'
            
        elif isinstance(first_dict[key] , str ):
            column_type = 'VARCHAR(255)'
            
        columns.append(f"{column_name} {column_type}")
    
    column_sql = ",\n".join(columns) 
    create_table = f"""CREATE TABLE IF NOT EXISTS {new_table_name}(
                         {column_sql} ); """
                        
    return create_table
    

    
    # for col in schema:
    #     col_name = col["column_name"]
    #     col_type = col["data_type"]
        
    #     if isinstance(test['วันเกิด'], (pd.Timestamp))
    #         col_type = 'TIMESTAMP'
        
    #     elif col_type == 'character varying' or col_type == str:
    #         col_type = 'VARCHAR(100)'
            
    #     elif col_type == 'text':
    #         col_type = 'TEXT'
        
    #     column.append(f"{col_name}  {col_type}")     #COLUMN DATATYPE
    # column_sql = ",\n".join(column)  #join will only add ,\n between string inside list 

    # create_table = f"""CREATE TABLE IF NOT EXISTS {new_table_name}(
    #                     {column_sql} ); """
                            
     
    # return create_table 


