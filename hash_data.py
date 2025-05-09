import hashlib
from Extract.extract_csv import fetch_csv
from Extract.extract_excel import fetch_excel
from Extract.extract_api import fetch_api

def deterministic_mask(value , salt="nuhospital"):
    return hashlib.sha256((salt + str(value)).encode()).hexdigest()

def format_preserving_mask(value , hashed):
    
    masked = ''
    index = 0
    
    for char in str(value):
        if char.isdigit():
            while not hashed[index].isdigit():
                index+=1
            masked+=hashed[index]
            index+=1
        elif char.isalpha():
            while not hashed[index].isalpha():
                index+=1
            masked+=hashed[index]
            index+=1
        else:
            masked+=char
            index+=1
                
    
    return masked


# hashed = deterministic_mask(123 , salt = "hospital")
# hashed = format_preserving_mask(123 , hashed)
# print(hashed)
#set pii index using dictionary
#USING LIST
# pii_index = {
#     'patient_name' : 4
# }



# def final_hashed(row , mask_field , salt = "hostpitalnu"):
#     mask = list(row)
#     for field in mask_field:
#         index = pii_index.get(field)
#         if index is not None and index < len(row):
#             hashed = deterministic_mask(row[index] , salt )
#             print("startformat")
#             mask[index] = format_preserving_mask(row[index] , hashed)
#             print(mask[index])
#     return mask

def final_hashed2(row , mask_field , salt = "hospitalnu"):
    copy_dict = row.copy()
    print("copydict success")
    
    print("enter loop")
    for field in mask_field:
        print("in loop")
        if field in copy_dict:
            hashed = deterministic_mask(copy_dict[field] , salt)
            copy_dict[field] = format_preserving_mask(copy_dict[field] , hashed)
    
    return copy_dict

    

mask_field = ['patient_name']  

# raw_data , head = fetch_excel('hospital_data.xlsx')
# raw_data = [dict(zip(head, row)) for row in raw_data]
# print(raw_data)

# def final_hashed3(row , mask_field , salt = "hospitalnu"):

def final_hashed3(row , mask_field , salt = "hospitalnu"):
    
    
    for field in mask_field:
        print("in loop")
        if field in row:
            print("in loop")
            print(f"before encode {row[field]}")
            original = row[field]
            row[field] = deterministic_mask(row[field] , salt )
            print(f"before format {row[field]}")
            fortmat_hashed = format_preserving_mask(original , row[field])
            print(f"after format {fortmat_hashed}")
            row[field] = fortmat_hashed
            print(row)
            return row
            
      
        else:print("invalid")
    
            
# rows = []
# for row in raw_data:
#     hash_row = final_hashed3(row , mask_field , salt = "hostpital")
#     rows.append(hash_row)
    
# print(rows)
