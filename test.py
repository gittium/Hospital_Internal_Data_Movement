
from Dynamic_Table.create_table import create_table
from connect import connection

conn = connection()


cur = conn.cursor()

cur.execute("""INSERT INTO hospital (hospital_name , hospital_branch , contact , patient_name)
VALUES ('Sirirat' , 'Bangkok' , '+6680' , 'Nattapong')""")
cur.execute("""INSERT INTO hospital (hospital_name , hospital_branch , contact , patient_name)
VALUES ('Sirirat' , 'indo' , '+6680' , 'sririrat')""")
conn.commit()
print("✅ load success")