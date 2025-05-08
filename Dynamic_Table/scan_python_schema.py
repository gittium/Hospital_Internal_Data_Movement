

# def scan_python_schema(cleaned_data , headers): 
#     first_row = cleaned_data[0]
     
#     data_type = []
#     column = []
#     for i ,  row in enumerate(first_row): 
#         d_type = type(first_row[i])
#         data_type.append(d_type)
        
#     for header in headers:
#         column.append(header)
        
#     tuple_data_type =(tuple(data_type))
#     tuple_column = (tuple(column))
#     tuple_pair = zip(tuple_column,tuple_data_type)


#     python_schema = []
#     for col , d_type in tuple_pair:
#         python_schema.append(
#             {"column_name" : col,
#             "data_type" : d_type
#             })
        
#     return python_schema





def scan_python_schema(cleaned_data, headers):
    first_row = cleaned_data[0]  # Get first dictionary
    print(f"first_row {first_row}")
    data_type = []
    column = []
    
    # Process dictionary values instead of enumerating
    for header in headers:
        d_type = type(first_row[header])
        data_type.append(d_type)
        column.append(header)
    
    tuple_data_type = tuple(data_type)
    tuple_column = tuple(column)
    tuple_pair = zip(tuple_column, tuple_data_type)

    python_schema = []
    for col, d_type in tuple_pair:
        python_schema.append({
            "column_name": col,
            "data_type": d_type
        })
    
    return python_schema


# data = [['Alice', '25', 'New York', '85.5'], ['Bob', '30', 'Los Angeles', '90.0'], ['Charlie', '35', 'Chicago', '78.0'], ['David', '40', 'Houston', '88.5'], ['Eva', '22', 'Phoenix', '92.0']]
# headers = ['name', 'age', 'city', 'score']
# cleaned_data = [dict(zip(headers, row)) for row in data]  # Convert to list of dictionaries
# print(cleaned_data)
# excel_data =[['Laptop', 1200, 50, 'Company A'], ['Smartphone', 800, 200, 'Company B'], ['Tablet', 300, 150, 'Company A'], ['Monitor', 250, 80, 'Company C'], ['Keyboard', 50, 300, 'Company D']]
# excel_headers = ['product_name', 'price', 'quantity', 'supplier']

#EXCEL
# ['Product', 'Price', 'Stock', 'Supplier']
# [['Laptop', 1200, 50, 'Company A'], ['Smartphone', 800, 200, 'Company B'], ['Tablet', 300, 150, 'Company A'], ['Monitor', 250, 80, 'Company C'], ['Keyboard', 50, 300, 'Company D']]


# cleaned_data = [[4, 'sirirat', 'petchbun', '080', 'pong_pong'], [5, 'Sirirat', 'Bangkok', '+6680', 'Nattapong'], [6, 'Sirirat', 'indo', '+6680', 'sririrat']]
# headers = ['id', 'hospital_name', 'hospital_branch', 'contact', 'patient_name']
# cleaned_data = [dict(zip(headers, row)) for row in cleaned_data]

# scan = scan_python_schema(cleaned_data, headers)
# print(scan)

