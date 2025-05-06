def upper_name(row):
    upper_row = row.upper()
    return upper_row

def standardize_contact(row):
    if row.startswith("0") :
        return "+66"+row[1:]
    
    if row.startswith("+66"):
        return row
    
    else :
        return row
    
def nine_address(row):
    if row.isalnum() :
        return "99999"
    else :
        return "888"
    


def tranform_data(raw_data):
    
    
    row = list(raw_data)
    row[1] = upper_name(row[1])
    row[2] = upper_name(row[2])
    row[3] = standardize_contact(row[3])
    row[4] = nine_address(row[4])
    
    return row



    