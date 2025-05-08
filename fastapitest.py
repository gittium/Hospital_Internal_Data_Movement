from fastapi import FastAPI
from fastapi.responses import JSONResponse
import random

app = FastAPI()

hospital_names = ["City Hospital", "General Health", "Metro Medical", "Sunrise Clinic"]
branches = ["Downtown", "East Wing", "North Campus", "West Side"]
contacts = ["1234567890", "9876543210", "5551234567", "4445678901"]
patient_names = ["Alice", "Bob", "Charlie", "Dana", "Evan"]

@app.get("/mock-patient")
def get_mock_patient():
    data = {
        "hospital_name": random.choice(hospital_names),
        "hostpital_branch": random.choice(branches),
        "contact": random.choice(contacts),
        "patient_name": random.choice(patient_names),
    },{
        "hospital_name": random.choice(hospital_names),
        "hostpital_branch": random.choice(branches),
        "contact": random.choice(contacts),
        "patient_name": random.choice(patient_names),
    },{
        "hospital_name": random.choice(hospital_names),
        "hostpital_branch": random.choice(branches),
        "contact": random.choice(contacts),
        "patient_name": random.choice(patient_names),
    }
    return JSONResponse(content=data)
