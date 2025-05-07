

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

