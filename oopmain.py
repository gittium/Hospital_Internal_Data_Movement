from Pipeline.pipeline import Pipeline
from Extract.oopcsv import ExtractCsv
from Extract.oopexcel import ExtractExcel
from Extract.oopapi import ExtractAPI
from Extract.connect import connection
from Extract.ooppostgres import ExtractPosgres


print("""
      Choose your Extractor
      1.CSV Extractor
      2.Excel Extractor
      3.API Extractor
      4.Postgres Extractor
      """)


option = input("enter source extract type:  ")


match option:
    
    case "1" : 
        file_name = input("enter file name:  ")
        extractor = ExtractCsv(file_name)
    
    case "2" : 
        file_name = input("enter file name:  ")
        extractor = ExtractExcel(file_name)
    
    case "3" : 
        url = input("enter API Address:  ")
        extractor = ExtractAPI(url)
        
    case "4" : 
        table_name = input("enter table name:  ")
        conn = connection()
        extractor = ExtractPosgres(table_name , conn)
    
    




if __name__ == "__main__":
    pipeline = (Pipeline(extractor))  #object
    pipeline.run()