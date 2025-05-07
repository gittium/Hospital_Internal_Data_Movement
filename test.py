
from Dynamic_Table.create_table import create_table
from connect import connection

conn = connection()


cleaned_data = [
    ["Sirirat", "CNX", "+6680", 999, "eaaf_fbad"]
]

headers = ["hospital_name", "branch", "contact", "address", "patient_name"]

test = create_table(cleaned_data , "test_dynamic_hospital" ,conn ,  headers)
print(test)