def validate_field_type(row):
    
   
    
    if not isinstance (row[1] , str ):
        raise ValueError(f"invalid type {row[1]} is not string")
    
    if not isinstance (row[2] , str ):
        raise ValueError(f"invalid type {row[2]} is not string")
    
    if not isinstance (row[3] , str ):
        raise ValueError(f"invalid type {row[3]} is not string")
    
    if not isinstance (row[4] , str ):
        raise ValueError(f"invalid type {row[4]} is not string")
    
    
def validate_empty(rows):
    
    for field in rows:
        if not str(field).strip():
            raise ValueError("got empty data")   
    
def validate_num_rows(row):
    expected_field = ["id" , "hospital_name" , "hospital_branch" , "contact" ,  "patient_name"]
    if len(row) != len(expected_field):
        raise ValueError(f"schema validation failed, exptected {len(expected_field)} rows got only {len(row)}: {row} " )