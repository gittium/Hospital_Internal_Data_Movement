Hello World this is my mini project for moving data between datasources for Internal Naresuan University Data

For now 5/13/2025 this is a demo version that i using local databasesources to testing and load the data

i also do some Data Privacy to cover PII data of patients by using hashlib to encode PII fields , format preserving mask to keep the shape of data appearance nearly original after done encoding

This is Postgres Database project
First before we start we need to install postgres on our local first

you can download it from their official sites with their documentation here : https://www.postgresql.org/download

after we installed them and their packages properly , setting connection we can move on to our project base

first we need to install pip to let we install any python packages we need in this project 

then we wil run

pip install -r requirements    --to install any packages we need

after that we need to placing some files before we extract it we can placed it in folder name DATA

and then we can run OUR MAIN FILE name : main_pipeline.py   to let the flow begin!!

after all the works now we will have the data we just threw it to DATA folder load into our Postgres Database we installed from the start .
