# 🎓 Student Dropout Prediction & Testing System

A machine learning-based web application that predicts whether a student is likely to **Dropout, remain Enrolled, or Graduate** based on academic and demographic information.

The project combines **Machine Learning, FastAPI, Pytest, and Playwright** to create and test a complete prediction system.

---

## 📌 Project Overview

Student dropout is an important challenge for educational institutions. Early identification of students who may be at risk can help institutions provide appropriate academic support.

This project uses the **UCI Student Dropout and Academic Success dataset** and builds a machine learning model to classify students into three categories:

* 🔴 Dropout
* 🟡 Enrolled
* 🟢 Graduate

The trained model is exposed through a **FastAPI REST API**, connected to a simple web interface, and tested using **Pytest and Playwright**.

---

## 🏗️ System Architecture

```text
                    Student Input
                         │
                         ▼
                  ┌──────────────┐
                  │   Web UI     │
                  │ HTML / CSS   │
                  │ JavaScript    │
                  └──────┬───────┘
                         │
                         │ HTTP POST
                         ▼
                  ┌──────────────┐
                  │   FastAPI    │
                  │ Prediction   │
                  │     API      │
                  └──────┬───────┘
                         │
                         ▼
                  ┌──────────────┐
                  │ ML Model     │
                  │ Decision Tree│
                  └──────┬───────┘
                         │
                         ▼
             ┌───────────────────────┐
             │ Prediction Result     │
             │ Dropout / Enrolled /  │
             │ Graduate              │
             └───────────────────────┘

       Testing
          │
          ├── Pytest → API Testing
          │
          └── Playwright → UI Automation
```

---

## 🚀 Technologies Used

| Technology          | Purpose                   |
| ------------------- | ------------------------- |
| Python              | Main programming language |
| Pandas              | Data processing           |
| Scikit-learn        | Machine learning          |
| Decision Tree       | Classification model      |
| Joblib              | Model serialization       |
| FastAPI             | REST API                  |
| Uvicorn             | API server                |
| HTML/CSS/JavaScript | User interface            |
| Pytest              | API testing               |
| Playwright          | UI automation             |
| Git/GitHub          | Version control           |

---

## 🤖 Machine Learning

### Dataset

The project uses the **UCI Student Dropout and Academic Success dataset**.

The dataset contains academic, demographic, socioeconomic, and enrollment-related information.

### Target Classes

The model predicts one of three classes:

```text
Dropout
Enrolled
Graduate
```

### Model

A **Decision Tree Classifier** is used for prediction.

The model is trained using:

* `train_test_split`
* `test_size = 0.2`
* `random_state = 42`
* Stratified train/test split
* Decision Tree with controlled depth

The trained model is saved using Joblib:

```text
ml/dropout_model.pkl
```

The target label encoder is saved as:

```text
ml/label_encoder.pkl
```

---

## 📊 Features

The model uses 36 input features, including:

* Marital status
* Application mode
* Application order
* Course
* Previous qualification
* Previous qualification grade
* Mother's qualification
* Father's qualification
* Admission grade
* Displaced status
* Debtor status
* Tuition fees status
* Gender
* Scholarship holder
* Age at enrollment
* International status
* First semester academic information
* Second semester academic information
* Unemployment rate
* Inflation rate
* GDP

---

## 🌐 FastAPI

The prediction model is exposed through a REST API.

### Start the API

Navigate to the API directory:

```bash
cd api
```

Run:

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

### API Documentation

FastAPI automatically provides interactive API documentation:

```text
http://localhost:8000/docs
```

### Health Check

```text
GET /health
```

Example response:

```json
{
  "status": "healthy"
}
```

### Prediction Endpoint

```text
POST /predict
```

The endpoint accepts student information and returns the predicted class.

Example response:

```json
{
  "prediction": "Graduate"
}
```

---

## 🖥️ Web UI

The project contains a simple web interface for entering student information.

Start the UI server:

```bash
cd ui
python -m http.server 5500
```

Open:

```text
http://localhost:5500/index.html
```

The user can enter student information and click **Predict**.

The UI sends the information to the FastAPI backend and displays the prediction.

Example:

```text
Prediction: Graduate
```

---

## 🧪 Testing

The project includes two types of automated testing.

### 1. API Testing with Pytest

The API tests verify:

* Home endpoint
* Health endpoint
* Prediction endpoint

Run:

```bash
pytest -v test/test_api.py
```

Expected result:

```text
3 passed
```

---

### 2. UI Testing with Playwright

Playwright automatically:

1. Opens the web application
2. Enters student information
3. Clicks the Predict button
4. Waits for the prediction
5. Verifies that a valid prediction is displayed

Run:

```bash
pytest -v -s test/test_ui.py
```

Example:

```text
UI Result: Prediction: Graduate
PASSED

1 passed
```

---

## 📁 Project Structure

```text
StudentDrop/
│
├── api/
│   ├── __init__.py
│   └── main.py
│
├── ml/
│   ├── train_model.py
│   ├── dropout_model.pkl
│   └── label_encoder.pkl
│
├── test/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_ui.py
│
├── ui/
│   └── index.html
│
├── Data/
│   └── data.csv
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/student-dropout-prediction-system.git
```

### 2. Navigate to the project

```bash
cd student-dropout-prediction-system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Install Playwright browsers

```bash
playwright install
```

---

## ▶️ Running the Complete Project

### Terminal 1 — FastAPI

```bash
cd api
python -m uvicorn main:app --reload
```

### Terminal 2 — Web UI

```bash
cd ui
python -m http.server 5500
```

### Terminal 3 — Tests

```bash
pytest -v
```

For UI testing:

```bash
pytest -v -s test/test_ui.py
```

---

## 🔄 Complete Workflow

```text
Student enters information
          ↓
       Web UI
          ↓
      FastAPI API
          ↓
   Data preprocessing
          ↓
    Decision Tree Model
          ↓
       Prediction
          ↓
Dropout / Enrolled / Graduate
          ↓
      Display in UI
```

Testing workflow:

```text
Pytest
  ↓
API Tests
  ↓
Endpoints verified


Playwright
  ↓
Open UI
  ↓
Enter student data
  ↓
Click Predict
  ↓
Verify prediction
```

---

## 🧪 Current Test Results

The project currently includes:

```text
API Tests
3 passed

Playwright UI Test
1 passed
```

All core API and UI testing workflows are functioning successfully.

---

## 🔮 Future Improvements

Possible future improvements include:

* Add a more advanced ML model comparison
* Improve model accuracy through hyperparameter tuning
* Add feature scaling and preprocessing pipelines
* Add prediction probability/confidence
* Improve the UI design
* Add database support
* Add authentication
* Add Docker deployment
* Deploy the FastAPI backend
* Deploy the frontend
* Add CI/CD using GitHub Actions
* Add more comprehensive automated tests

---

## 🎯 Project Objective

The main objective of this project is to demonstrate an end-to-end machine learning application that combines:

```text
Machine Learning
        +
REST API
        +
Web Interface
        +
Automated API Testing
        +
Automated UI Testing
```

This project demonstrates practical experience in **ML model development, API development, software testing, and automation**.

---

## 📚 Dataset

Dataset source:

**UCI Student Dropout and Academic Success Dataset**

The dataset was originally provided by the UCI Machine Learning Repository.

Please check the dataset's license and usage terms before redistributing the dataset with a public repository.

---

## 👩‍💻 Author

**Pooja Choudhary**

B.Tech — Computer Science / Business Systems

GitHub:
`https://github.com/Pooja-20050802`

---
