import psycopg2
import pandas as pd
from connect import connection


def extract_postgres(table):
    try:
        conn = connection()
        print("connection_success")
        
    except Exception as e :
        print("error" , e)
        print("connection fail")
        
    cur = conn.cursor()
    
    
    query = f"SELECT * FROM {table};"

    
    cur.execute(query)
    

    
    conn.commit
    
    
    data = cur.fetchall()  # fetch list of tuples
    
    
    # cur.execute(
    #         """ALTER TABLE hospital ALTER COLUMN "วันเกิด" TYPE DATE USING TO_DATE("วันเกิด", 'YYYY-MM-DD');
    #         ALTER TABLE hospital ALTER COLUMN "วันที่เข้ารักษา" TYPE DATE USING TO_DATE("วันที่เข้ารักษา", 'YYYY-MM-DD');
    #         ALTER TABLE hospital ALTER COLUMN "วันที่จำหน่าย" TYPE DATE USING TO_DATE("วันที่จำหน่าย", 'YYYY-MM-DD');"""
    #     )
    # conn.commit()
    
    
    
    list_datas = []
    
    for i in data:
        list_data = list(i)
        # convert tuple to list
        list_datas.append(list_data)  # append to data list
      # list of list
    
    # print(list_datas)
    
    # datetime = ['วันเกิด' , 'วันที่เข้ารักษา' , 'วันที่จำหน่าย']
    # for date in datetime:
    #     df[date] = pd.to_datetime(df[date])
    # print(df.dtypes)


    
   
    
    
    
    query = """SELECT column_name , data_type 
                from information_schema.columns
                WHERE table_name = %s
                ORDER BY ordinal_position;"""
    
    
    cur.execute(query , (table,) )  # (table,)   "," after table make this a tuple
    output = cur.fetchall()
    
    #[('รหัสผู้ป่วย', 'character varying'), ('ชื่อนามสกุล', 'character varying'), ('รหัสบัตรประชาชน', 'character varying'), ('วันเกิด', 'date'), (          ('เพศ', 'character varying'), ('เบอร์โทรศัพท์', 'character varying'), ('อีเมล', 'character varying'), ('ที่อยู่', 'text'), ('โรคประจำตัว', 'ch        haracter varying'), ('เลขกรมธรรม์', 'character varying'), ('วันที่เข้ารักษา', 'date'), ('วันที่จำหน่าย', 'date')]
      # fetch list of tuples
     # output is now list of tuple  [(col , dt),(col , dt)]
    header = []
    for tuple in output:
        list_tuple = list(tuple)
        
        for char in list_tuple:
            if list_tuple.index(char) == 0:
                header.append(char)
            continue
    

    return list_datas , header 

row, header = extract_postgres('hospital')    
print(row)
print(header)

# rows , header = extract_postgres('hospital')
# for row in rows:
#     for i in row:
#         # print(i)
    
        
    
        
    # cur.close()
    # print("cur extract closed")
    # conn.close()
    # print("conn extract closed")    
    
    # return list_datas , header


   