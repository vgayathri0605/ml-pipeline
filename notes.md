📘 Version 6 — Dynamic ML Pipeline Notes
🔷 Project Goal

Build a dynamic, production-style ML pipeline with:

Config-driven design

Dynamic file ingestion

Model training

Model versioning

Logging

Future: S3 + Lambda automation

🔷 What Makes Version 6 Different (Upgrade)
Feature	Previous Versions	Version 6
File handling	Static	Dynamic (latest file auto-detected)
Pipeline	Single script	Modular architecture
ML	Minimal/none	Integrated ML training
Logging	print()	Structured logging
Config	Hardcoded	YAML-based config
Deployment thinking	Low	MLOps-oriented
🔷 Step 0 — Project Setup
Created Folder Structure

ml_pipeline_v6/

config/

data/

incoming/

processed/

models/

logs/

src/

Concept:

Organized structure = industry standard

Separation of concerns (data, models, code)

🔷 Step 1 — Virtual Environment
Commands Used

python -m venv venv
.\venv\Scripts\Activate
pip install pandas scikit-learn pyyaml joblib boto3
pip freeze > requirements.txt

Concepts:
✅ Virtual Environment

Isolated Python environment

Avoids dependency conflicts

✅ requirements.txt

Stores project dependencies

Ensures reproducibility

🔷 Step 2 — Config-Driven Design
File: config/config.yaml

Defines:

Data paths

Model settings

Logging path

Concept:
❌ Hardcoded

Values written directly in code
Example:
pd.read_csv("data/incoming/file.csv")

✅ Config-driven

Values stored externally in YAML

Benefits:

Flexible

Easy to update

Production standard

🔷 Step 3 — Logging System
File: src/logger.py
Purpose:

Track pipeline execution

Store logs in file instead of printing

Concepts:
✅ Logging vs Print
Print	Logging
Temporary	Persistent
Console only	Stored in file
Not scalable	Production-ready
✅ Log Levels

INFO → normal steps

ERROR → failures

✅ Log Format

Includes:

Timestamp

Log level

Message

Example:
2026-03-17 10:30:22 - INFO - Pipeline started

---

## 🔷 Step 4 — Dynamic Data Ingestion

### File: src/ingest.py

### Purpose:

Automatically detect and load the **latest CSV file** from the input folder.

### Key Logic:

* Read all files from directory
* Filter only `.csv` files
* Identify latest file using creation time
* Load data using pandas

### Concepts:

#### ✅ Dynamic File Handling

* No need to hardcode file names
* Pipeline automatically adapts to new incoming data

#### ✅ os.listdir()

* Lists all files in a directory

#### ✅ File Filtering

* Select only relevant files (CSV)

#### ✅ os.path.getctime()

* Gets file creation time
* Helps identify latest file

#### ✅ max(..., key=...)

* Used to select newest file

### Why This is Important:

* Simulates real-world data pipelines
* Handles continuously incoming data
* Removes manual intervention

### Resume Value:

* “Implemented dynamic data ingestion by automatically detecting and processing latest files from input source.”

---

## 🔷 Step 5 — Data Preprocessing

### File: src/preprocess.py

### Purpose:

Prepare raw data for machine learning model training.

### Steps Performed:

* Remove missing values
* Split dataset into features (X) and target (y)

### Concepts:

#### ✅ Handling Missing Data

* Using `dropna()` to remove incomplete rows

#### ✅ Feature-Target Split

* X → Input features (independent variables)
* y → Target variable (dependent/output)

#### ✅ iloc Indexing

* `df.iloc[:, :-1]` → all columns except last
* `df.iloc[:, -1]` → last column

### Why This is Important:

* ML models require clean, structured data
* Separating X and y is fundamental for training

### Resume Value:

* “Performed data preprocessing including handling missing values and preparing feature-target datasets for model training.”

---

## 🔷 Key Learning So Far (Updated)

* Built dynamic ingestion system
* Understood real-world file handling
* Learned preprocessing for ML readiness
* Connected data pipeline → ML pipeline

---
---

## 🔷 Step 6 — Model Training

### File: src/train.py

### Purpose:

Train a machine learning model using prepared data.

### Model Used:

* Linear Regression (from scikit-learn)

### Steps:

* Initialize model
* Train model using `.fit(X, y)`
* Return trained model

### Concepts:

#### ✅ Machine Learning Model

* Learns relationship between input (X) and output (y)

#### ✅ Model Training

* `.fit(X, y)` trains model using data

#### ✅ scikit-learn

* Popular Python ML library

### Why This is Important:

* Introduces intelligence into pipeline
* Converts data pipeline → ML pipeline

### Resume Value:

* “Integrated machine learning model training using scikit-learn within the pipeline.”

---
---

## 🔷 Step 7 — Model Versioning

### File: src/versioning.py

### Purpose:

Save trained models with unique versions instead of overwriting.

### Approach:

* Generate timestamp-based version
* Save model using joblib
* Store in models folder

### Concepts:

#### ✅ Model Versioning

* Each model run is saved separately
* Enables tracking and comparison

#### ✅ Timestamp-based Naming

* Format: YYYYMMDD_HHMMSS
* Ensures uniqueness

#### ✅ joblib

* Used to serialize (save) ML models

### Why This is Important:

* Prevents overwriting models
* Supports reproducibility
* Core MLOps concept

### Resume Value:

* “Implemented model versioning using timestamp-based storage for tracking and reproducibility.”

---
---

## 🔷 Step 8 — Pipeline Orchestration

### File: src/pipeline.py

### Purpose:

Integrate all components into a single end-to-end pipeline.

### Flow:

1. Load configuration
2. Initialize logger
3. Load latest data file
4. Preprocess data
5. Train ML model
6. Save versioned model
7. Log all steps

### Concepts:

#### ✅ Orchestration

* Combining multiple modules into one workflow

#### ✅ Modular Architecture

* Separate files for each functionality
* Improves maintainability and scalability

#### ✅ Exception Handling

* try/except used to catch failures
* Errors logged for debugging

### Why This is Important:

* Simulates real-world ML systems
* Moves from scripts → production pipeline

### Output:

* Model saved in `/models`
* Logs stored in `/logs/pipeline.log`

### Resume Value:

* “Designed and implemented an end-to-end ML pipeline integrating ingestion, preprocessing, model training, versioning, and logging using a modular architecture.”

---
---

## 🔷 Step 9 — S3 Integration

### Files:

* src/s3_utils.py
* Updated pipeline.py

### Purpose:

Integrate cloud storage (AWS S3) for dynamic data ingestion.

### Steps:

* Connected to S3 using boto3
* Retrieved list of files in bucket
* Identified latest file using LastModified
* Downloaded file locally
* Used downloaded file for pipeline processing

### Concepts:

#### ✅ AWS S3

* Cloud storage service
* Stores input data for pipeline

#### ✅ boto3

* Python SDK for AWS
* Used to interact with S3

#### ✅ Cloud-based Ingestion

* Replaces local file dependency
* Enables real-time data pipelines

### Why This is Important:

* Moves pipeline from local → cloud
* Aligns with real-world data systems
* Enables scalability

### Resume Value:

* “Integrated AWS S3 for dynamic data ingestion using boto3, enabling cloud-based ML pipeline execution.”

---
---

## 🔷 Step 10 — Lambda Trigger (Event-Driven Architecture)

### File:

* lambda_function.py

### Purpose:

Trigger ML pipeline automatically when a new file is uploaded to S3.

### Implementation:

* Created Lambda handler function
* Called `run_pipeline()` inside Lambda
* Simulated event-driven execution locally

### Concepts:

#### ✅ AWS Lambda

* Serverless compute service
* Executes code based on events

#### ✅ Event-Driven Architecture

* System reacts to events (e.g., file upload)
* No manual execution required

#### ✅ Lambda Handler

* Entry point for Lambda execution
* Accepts `event` and `context`

### Why This is Important:

* Enables full automation of ML pipeline
* Aligns with real-world cloud architectures
* Reduces manual intervention

### Limitation:

* Full deployment requires packaging dependencies (pandas, sklearn)

### Resume Value:

* “Designed an event-driven ML pipeline using AWS Lambda to trigger execution upon S3 file uploads.”

---

## 🔷 FINAL PROJECT SUMMARY

### 🔹 End-to-End Flow:

S3 (data upload)
↓
Lambda Trigger
↓
Pipeline Execution
↓

* Data ingestion
* Preprocessing
* Model training
* Model versioning
* Logging

---

## 🔷 Key Concepts Covered

### 🔹 Data Engineering

* Dynamic file ingestion
* Data preprocessing

### 🔹 Machine Learning

* Feature-target split
* Model training (Linear Regression)

### 🔹 MLOps

* Model versioning
* Logging
* Config-driven pipeline

### 🔹 Cloud

* AWS S3 integration
* Lambda trigger (event-driven)

---

## 🔷 Resume Keywords

* Dynamic ML Pipeline
* Config-driven architecture
* AWS S3 integration
* Event-driven processing
* Model versioning
* Logging and monitoring
* Modular pipeline design

---

## 🔷 Personal Understanding

This project helped me:

* Move from ETL → ML systems
* Understand real-world pipeline design
* Learn basics of MLOps
* Work with cloud-based data flow

---
