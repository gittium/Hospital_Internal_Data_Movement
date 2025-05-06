import psycopg2



def extract_data():
    try:
        conn = psycopg2.connect(host="localhost", port="5432" , user="postgres" , password="admin" , dbname="postgres")
        print("connection_success")
        
    except Exception as e :
        print("error" , e)
        print("connection fail")
        
    cur = conn.cursor()
    
    
    cur.execute("SELECT * FROM hospital;")
    
    data = cur.fetchall()
    
   
        
    
        
    cur.close()
    print("cur extract closed")
    conn.close()
    print("conn extract closed")
    
    return data


