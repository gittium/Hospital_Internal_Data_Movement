
from Dynamic_Table.create_table import create_table
from connect import connection
from Extract.extract_csv import fetch_csv
from error_handling import validate_field_type , validate_empty
conn = connection()


cur = conn.cursor()

rows , head = fetch_csv('hospital_data.csv')
list_row = [dict(zip(head,row)) for row in rows ]

for row in list_row:
    
    validate_empty(row)