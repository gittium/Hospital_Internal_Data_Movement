from fastapi import FastAPI
from fastapi.responses import JSONResponse
import random
from faker import Faker

app = FastAPI()
fake = Faker('th_TH')  # Use Thai locale for realistic data


medical_conditions = ["เบาหวาน", "ความดันสูง", "โรคหัวใจ", "มะเร็ง", "หอบหืด", "สุขภาพดี"]

@app.get("/mock-patient")
def get_mock_patient():
    patients = []
    for i in range(1, 4):
        patient = {
            "รหัสผู้ป่วย": f"PAT{i:04}",
            "ชื่อ-นามสกุล": fake.name(),
            "รหัสบัตรประชาชน": fake.ssn(),
            "วันเกิด": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
            "เพศ": random.choice(["ชาย", "หญิง"]),
            "เบอร์โทรศัพท์": fake.phone_number(),
            "อีเมล": fake.email(),
            "ที่อยู่": fake.address().replace("\n", " "),
            "โรคประจำตัว": random.choice(medical_conditions),
            "เลขกรมธรรม์": fake.bothify(text='INS-########'),
            "วันที่เข้ารักษา": fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d'),
            "วันที่จำหน่าย": fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
            
        }
        patients.append(patient)

    return JSONResponse(content=patients)
