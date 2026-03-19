# 🚀 Dynamic ML Pipeline (Version 6)

## 📌 Overview

This project implements an end-to-end Machine Learning pipeline with dynamic data ingestion, model training, versioning, and logging using Python and AWS.

---

## ⚙️ Key Features

* Dynamic data ingestion from AWS S3
* Data preprocessing (handling missing values, feature-target split)
* Machine Learning model training (Linear Regression)
* Model versioning using timestamp-based naming
* Logging system for pipeline monitoring
* Modular architecture for scalability and maintainability
* Event-driven pipeline design using AWS Lambda (simulated)

---

## 🏗️ Architecture

S3 (Data Upload)
↓
Download Latest File
↓
Pipeline Execution

* Data Ingestion
* Preprocessing
* Model Training
* Model Versioning
* Logging

---

## 📂 Project Structure

ml_pipeline_v6/
│
├── config/
├── data/
├── src/
│   ├── ingest.py
│   ├── preprocess.py
│   ├── train.py
│   ├── versioning.py
│   ├── logger.py
│   ├── s3_utils.py
│   └── pipeline.py
│
├── lambda_function.py
├── requirements.txt
└── README.md

---

## 🧠 Technologies Used

* Python
* Pandas
* Scikit-learn
* AWS S3
* AWS Lambda (conceptual)
* Boto3

---

## ▶️ How to Run

```bash
python -c "from src.pipeline import run_pipeline; run_pipeline()"
```

---

## 📊 Output

* Versioned models saved in `/models`
* Logs stored in `/logs/pipeline.log`

---

## 🚀 Future Improvements

* Model evaluation & comparison
* API deployment using FastAPI
* CI/CD integration
* Full Lambda deployment

---

## 💡 Key Highlights

* Designed a dynamic ML pipeline with automated data ingestion
* Implemented cloud-based processing using AWS S3
* Applied MLOps concepts such as versioning and logging
* Built a modular and scalable architecture

---
