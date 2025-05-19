import hashlib
# from Extract.extract_csv import fetch_csv
# from Extract.extract_excel import fetch_excel
# from Extract.extract_api import fetch_api
# from Extract.extract_postgres import extract_postgres



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






# mask_field = ['ชื่อนามสกุล','รหัสบัตรประชาชน' ,'เลขกรมธรรม์']  



def final_hashed(row , mask_field , salt = "hospitalnu"):


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

            

        else:print("invalid")
    return row
    
            


# rows , header = extract_postgres('hospital')  

# dict_row = [dict(zip(header, row)) for row in rows]

# for row in dict_row:
#     print(final_hashed(row, mask_field , salt="nuhos"))