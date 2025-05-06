import psycopg2




conn = psycopg2.connect(host="localhost", port="5432" , user="postgres" , password="admin" , dbname="postgres")
print("connection_success")

def scan_table(table , conn):
    cur = conn.cursor()
    
    
    query = """SELECT column_name , data_type 
                from information_schema.columns
                WHERE table_name = %s
                ORDER BY ordinal_position;"""
    
    
    cur.execute(query , (table,) )  # (table,)   "," after table make this a tuple
    output = cur.fetchall()  # output is now list of tuple  [(col , dt),(col , dt)]
    
    
   
    schema = []    # create list to return data scanning

    for column_name , data_type in  output:
        schema.append({
            "column_name" : column_name,
            "data_type" : data_type
        })
    print(schema)
    cur.close()
    return schema

scan_table("hospital" , conn)
    
    
    