import psycopg2
from leanbasic.ETL.Dynamic_Table.create_table import create_table

def load_data(cleaned_data):
    
    conn = psycopg2.connect(host = "localhost" , port = "5432" , user = "postgres" , password = "admin" , dbname = "postgres")
    print("load connection success")
    
    cur = conn.cursor()
    
    
    
    
    
    for row in cleaned_data:
        cur.execute("INSERT INTO cleaned_data(hospital_name , hospital_branch , contact , address , patient_name) VALUES(%s ,%s , %s , %s , %s);",(row[1] , row[2] , row[3] , row[4] , row[5]))
    
    conn.commit()
    print("load success")
    cur.close()
    print("load cursur() closed")
    conn.close
    print("load connection closed")