



def gen_sql_table(new_table_name , schema):
    column = []
    
    
    
    for col in schema:
        col_name = col["column_name"]
        col_type = col["data_type"]
        
        if col_type == 'integer' or col_type == int:
            col_type = 'INTEGER'
        
        elif col_type == 'character varying' or col_type == str:
            col_type = 'VARCHAR(100)'
            
        elif col_type == 'text':
            col_type = 'TEXT'
        
        column.append(f"{col_name}  {col_type}")     #COLUMN DATATYPE
    column_sql = ",\n".join(column)  #join will only add ,\n between string inside list 

    create_table = f"""CREATE TABLE IF NOT EXISTS {new_table_name}(
                        {column_sql} ); """
                            
     
    return create_table 


