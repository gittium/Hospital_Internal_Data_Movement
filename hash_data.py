import hashlib


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
pii_index = {
    'patient_name' : 5
}



def final_hashed(row , mask_field , salt = "hostpitalnu"):
    mask = list(row)
    for field in mask_field:
        index = pii_index.get(field)
        if index is not None and index < len(row):
            hashed = deterministic_mask(row[index] , salt )
            print("startformat")
            mask[index] = format_preserving_mask(row[index] , hashed)
            print(mask[index])
    return mask




    
