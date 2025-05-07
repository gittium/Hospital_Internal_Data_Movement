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
    

    


# def tranform_data(raw_data):
    

    
    
#     rows = list(raw_data)
    
#     list_row_dict = []
    
#     for row in rows:
#         row_dict = {
#         'hospital_name' : upper_name(row[0]),
#         'hospital_branch' : upper_name(row[1]),
#         'contact' : standardize_contact(row[2]),
#         'patient_name' : nine_address(row[3])
#         }
#         list_row_dict.append(row_dict)
    
#     return list_row_dict



# cleaned_data = [
#     ["Sirirat", "CNX", "+6680",  "eaaf_fbad"],
#     ["Sirirat", "CNX", "+6680", "eaaf_fbad"],
#     ["Sirirat", "CNX", "+6680",  "eaaf_fbad"]
# ]
# print(tranform_data(cleaned_data))
def tranform_data(raw_data):
    # Single row is passed, no need to convert to list
    row_dict = {
        'hospital_name': upper_name(raw_data[1]),
        'hospital_branch': upper_name(raw_data[2]),
        'contact': standardize_contact(raw_data[3]),
        'patient_name': raw_data[4]
    }
    
    return row_dict