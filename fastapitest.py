from fastapi import FastAPI
from fastapi.responses import JSONResponse
import random

app = FastAPI()

hospital_names = ["City Hospital", "General Health", "Metro Medical", "Sunrise Clinic"]
branches = ["Downtown", "East Wing", "North Campus", "West Side"]
contacts = [801234562,801234567,801234547]
patient_names = ["Alice", "Bob", "Charlie", "Dana", "Evan"]

@app.get("/mock-patient")
def get_mock_patient():
    data = {
        "id" : 1 ,
        "hospital_name": random.choice(hospital_names),
        "hospital_branch": random.choice(branches),
        "contact": random.choice(contacts),
        "patient_name": random.choice(patient_names),
    },{
        "id" : 2,
        "hospital_name": random.choice(hospital_names),
        "hospital_branch": random.choice(branches),
        "contact": random.choice(contacts),
        "patient_name": random.choice(patient_names),
    },{ "id" : 3,
        "hospital_name": random.choice(hospital_names),
        "hospital_branch": random.choice(branches),
        "contact": random.choice(contacts),
        "patient_name": random.choice(patient_names),
    }
    return JSONResponse(content=data)
