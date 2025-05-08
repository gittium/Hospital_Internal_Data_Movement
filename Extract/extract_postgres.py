import psycopg2



def extract_postgres(table):
    try:
        conn = psycopg2.connect(host="localhost", port="5432" , user="postgres" , password="admin" , dbname="postgres")
        print("connection_success")
        
    except Exception as e :
        print("error" , e)
        print("connection fail")
        
    cur = conn.cursor()
    
    query = f"SELECT * FROM {table};"
    
    cur.execute(query)
    
    
    data = cur.fetchall()  # fetch list of tuples
    list_datas = []
    for i in data:
        list_data = list(i)
        # convert tuple to list
        list_datas.append(list_data)  # append to data list
      # list of list
    
    
   
    
    
    
    query = """SELECT column_name , data_type 
                from information_schema.columns
                WHERE table_name = %s
                ORDER BY ordinal_position;"""
    
    
    cur.execute(query , (table,) )  # (table,)   "," after table make this a tuple
    output = cur.fetchall()
      # fetch list of tuples
     # output is now list of tuple  [(col , dt),(col , dt)]
    header = []
    for tuple in output:
        list_tuple = list(tuple)
        for char in list_tuple:
            if list_tuple.index(char) ==0:
                header.append(char)
            continue
    
    
        
        
    
        
    cur.close()
    print("cur extract closed")
    conn.close()
    print("conn extract closed")    
    
    return list_datas , header


   