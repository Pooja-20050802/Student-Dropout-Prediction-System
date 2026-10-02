from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path


app = FastAPI(
    title="Student Dropout Prediction API",
    description="Predicts whether a student will Dropout, remain Enrolled, or Graduate.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load trained model and label encoder
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "ml"

model = joblib.load(MODEL_DIR / "dropout_model.pkl")
label_encoder = joblib.load(MODEL_DIR / "label_encoder.pkl")


# Input schema
class StudentData(BaseModel):
    marital_status: int
    application_mode: int
    application_order: int
    course: int
    daytime_evening_attendance: int
    previous_qualification: int
    previous_qualification_grade: float
    nationality: int
    mothers_qualification: int
    fathers_qualification: int
    mothers_occupation: int
    fathers_occupation: int
    admission_grade: float
    displaced: int
    educational_special_needs: int
    debtor: int
    tuition_fees_up_to_date: int
    gender: int
    scholarship_holder: int
    age_at_enrollment: int
    international: int

    curricular_units_1st_sem_credited: int
    curricular_units_1st_sem_enrolled: int
    curricular_units_1st_sem_evaluations: int
    curricular_units_1st_sem_approved: int
    curricular_units_1st_sem_grade: float
    curricular_units_1st_sem_without_evaluations: int

    curricular_units_2nd_sem_credited: int
    curricular_units_2nd_sem_enrolled: int
    curricular_units_2nd_sem_evaluations: int
    curricular_units_2nd_sem_approved: int
    curricular_units_2nd_sem_grade: float
    curricular_units_2nd_sem_without_evaluations: int

    unemployment_rate: float
    inflation_rate: float
    gdp: float


@app.get("/")
def home():
    return {
        "message": "Student Dropout Prediction API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict(data: StudentData):

    input_data = pd.DataFrame([{
        "Marital status": data.marital_status,
        "Application mode": data.application_mode,
        "Application order": data.application_order,
        "Course": data.course,
        "Daytime/evening attendance": data.daytime_evening_attendance,
        "Previous qualification": data.previous_qualification,
        "Previous qualification (grade)": data.previous_qualification_grade,
        "Nacionality": data.nationality,
        "Mother's qualification": data.mothers_qualification,
        "Father's qualification": data.fathers_qualification,
        "Mother's occupation": data.mothers_occupation,
        "Father's occupation": data.fathers_occupation,
        "Admission grade": data.admission_grade,
        "Displaced": data.displaced,
        "Educational special needs": data.educational_special_needs,
        "Debtor": data.debtor,
        "Tuition fees up to date": data.tuition_fees_up_to_date,
        "Gender": data.gender,
        "Scholarship holder": data.scholarship_holder,
        "Age at enrollment": data.age_at_enrollment,
        "International": data.international,

        "Curricular units 1st sem (credited)": data.curricular_units_1st_sem_credited,
        "Curricular units 1st sem (enrolled)": data.curricular_units_1st_sem_enrolled,
        "Curricular units 1st sem (evaluations)": data.curricular_units_1st_sem_evaluations,
        "Curricular units 1st sem (approved)": data.curricular_units_1st_sem_approved,
        "Curricular units 1st sem (grade)": data.curricular_units_1st_sem_grade,
        "Curricular units 1st sem (without evaluations)": data.curricular_units_1st_sem_without_evaluations,

        "Curricular units 2nd sem (credited)": data.curricular_units_2nd_sem_credited,
        "Curricular units 2nd sem (enrolled)": data.curricular_units_2nd_sem_enrolled,
        "Curricular units 2nd sem (evaluations)": data.curricular_units_2nd_sem_evaluations,
        "Curricular units 2nd sem (approved)": data.curricular_units_2nd_sem_approved,
        "Curricular units 2nd sem (grade)": data.curricular_units_2nd_sem_grade,
        "Curricular units 2nd sem (without evaluations)": data.curricular_units_2nd_sem_without_evaluations,

        "Unemployment rate": data.unemployment_rate,
        "Inflation rate": data.inflation_rate,
        "GDP": data.gdp
    }])

    prediction = model.predict(input_data)

    predicted_class = label_encoder.inverse_transform(prediction)[0]

    return {
        "prediction": predicted_class
    }