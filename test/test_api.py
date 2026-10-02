from fastapi.testclient import TestClient
from api.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Student Dropout Prediction API is running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_prediction():
    student = {
        "marital_status": 1,
        "application_mode": 17,
        "application_order": 1,
        "course": 171,
        "daytime_evening_attendance": 1,
        "previous_qualification": 1,
        "previous_qualification_grade": 122.0,
        "nationality": 1,
        "mothers_qualification": 13,
        "fathers_qualification": 10,
        "mothers_occupation": 6,
        "fathers_occupation": 5,
        "admission_grade": 127.3,
        "displaced": 1,
        "educational_special_needs": 0,
        "debtor": 0,
        "tuition_fees_up_to_date": 1,
        "gender": 1,
        "scholarship_holder": 0,
        "age_at_enrollment": 20,
        "international": 0,

        "curricular_units_1st_sem_credited": 0,
        "curricular_units_1st_sem_enrolled": 6,
        "curricular_units_1st_sem_evaluations": 6,
        "curricular_units_1st_sem_approved": 6,
        "curricular_units_1st_sem_grade": 13.5,
        "curricular_units_1st_sem_without_evaluations": 0,

        "curricular_units_2nd_sem_credited": 0,
        "curricular_units_2nd_sem_enrolled": 6,
        "curricular_units_2nd_sem_evaluations": 6,
        "curricular_units_2nd_sem_approved": 5,
        "curricular_units_2nd_sem_grade": 12.5,
        "curricular_units_2nd_sem_without_evaluations": 0,

        "unemployment_rate": 11.1,
        "inflation_rate": 0.6,
        "gdp": 2.02
    }

    response = client.post("/predict", json=student)

    assert response.status_code == 200

    result = response.json()

    assert "prediction" in result
    assert result["prediction"] in [
        "Dropout",
        "Enrolled",
        "Graduate"
    ]