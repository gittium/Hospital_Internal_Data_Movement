import psycopg2

def connection():
    try:
        conn = psycopg2.connect(host="localhost", port="5432" , user="postgres" , password="admin" , dbname="postgres")
        print("connection_success")
        return conn
        
    except Exception as e : 
        print("connection failed" , e)
        
        
    