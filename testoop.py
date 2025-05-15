from Extract.oopapi import ExtractAPI
from Extract.ooppostgres import ExtractPosgres
from Extract.connect import connection


# print(ExtractAPI('http://127.0.0.1:8000/mock-patient').extract())

conn = connection()
print(ExtractPosgres("hospital" , conn).extract())