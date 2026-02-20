# Retail Sales ETL Pipeline using Apache Airflow

A production-style ETL pipeline built using:

- Apache Airflow 2.9+
- Python 3.12
- MySQL / MariaDB
- Pandas
- Ubuntu Linux

This project demonstrates a complete Extract–Transform–Load workflow orchestrated using Airflow DAGs.

---

## Project Architecture

Data Source (CSV)
        ↓
Extract (Airflow Task)
        ↓
Transform (Data Cleaning + Calculations)
        ↓
Load (Insert into MySQL)
        ↓
Aggregate (Generate Sales Summary)

---

## Project Structure

```
etl_airflow_project/
│
├── pipeline.py
├── db_config.py
├── requirements.txt
├── README.md
│
├── data/
│   └── retail_sales.csv
│
└── dags/
    └── retail_etl_dag.py
```

---

## Features

- Extract retail sales data from CSV
- Transform and compute total_amount
- Load cleaned data into MySQL
- Aggregate total revenue into summary table
- Fully orchestrated using Airflow
- Idempotent (No duplicate inserts)
- Clean modular design

---

## Database Schema

### retail_sales

| Column | Type |
|--------|------|
| order_id | INT |
| customer_name | VARCHAR |
| product_name | VARCHAR |
| quantity | INT |
| price | DECIMAL |
| total_amount | DECIMAL |

### sales_summary

| Column | Type |
|--------|------|
| id | INT (Auto Increment) |
| total_orders | INT |
| total_revenue | DECIMAL |
| created_at | TIMESTAMP |

---

## DAG Details

- DAG ID: `retail_sales_etl`
- Schedule: Daily
- Tasks:
  - extract_task
  - transform_task
  - load_task
  - aggregate_task

---

## Technologies Used

- Python
- Apache Airflow
- Pandas
- MySQL Connector
- Ubuntu Linux

---

## Setup Instructions

1. Create Python virtual environment
2. Install requirements
3. Configure MySQL database
4. Place DAG inside Airflow dags folder
5. Start Airflow scheduler and webserver
6. Trigger DAG

---

## How to Run

```bash
airflow scheduler
airflow webserver --port 8080
airflow dags trigger retail_sales_etl
```

---

## Learning Outcomes

- Building ETL pipelines
- Airflow DAG orchestration
- MySQL integration
- Production-safe path handling
- Idempotent data loading
- XCom usage between tasks

---

## Project Screenshot

-- Execution of all tasks (success) state

<img width="1920" height="1080" alt="Screenshot (78)" src="https://github.com/user-attachments/assets/83c0b4b3-31bf-4c95-95cf-3669d5a12f61" />

## Author

Paul  
Data Engineering & Backend Developer
