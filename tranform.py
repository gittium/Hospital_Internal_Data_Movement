from hash_data import final_hashed

class Tranform:

    def __init__(self , row ,mask_fields ):
        self.row = row
        self.mask_fields = mask_fields

    

    def standardize_contact(self):
       
            if self.row['เบอร์โทรศัพท์'].startswith("66") :
                return "0"+self.row['เบอร์โทรศัพท์'][1:]
            
            elif self.row['เบอร์โทรศัพท์'].startswith("+66"):
                return "0"+self.row['เบอร์โทรศัพท์'][1:]
            
            elif self.row['เบอร์โทรศัพท์'].startswith("0") == False:
                return "0"+self.row['เบอร์โทรศัพท์']
            
            elif "-"  in self.row['เบอร์โทรศัพท์']:
                split_contact = self.row['เบอร์โทรศัพท์'].split("-")
                clean_contact = "".join(split_contact)
                
                return clean_contact
            
            elif "_"  in self.row['เบอร์โทรศัพท์']:
                
                split_contact = self.row['เบอร์โทรศัพท์'].split("_")
                clean_contact = "".join(split_contact)
                
                return clean_contact

    
    
    


    def tranform_data(self):
        # Single row is passed, no need to convert to list
        self.row['เบอร์โทรศัพท์'] = self.standardize_contact()
        hashed = final_hashed(self.row, self.mask_fields , salt="nuhos")
        
        
        return hashed

    

    # mask_field = ['ชื่อนามสกุล','รหัสบัตรประชาชน' ,'เลขกรมธรรม์']  



    