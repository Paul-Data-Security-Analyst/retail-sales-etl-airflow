import pandas as pd
import mysql.connector
from db_config import DB_CONFIG

# HARD absolute path (NO os.getlogin, NO dynamic replacement)
CSV_PATH = "/home/ubuntu/etl_airflow_project/data/retail_sales.csv"


def extract():
    df = pd.read_csv(CSV_PATH)
    print("Extraction successful")
    return df.to_dict()


def transform(ti):
    data = ti.xcom_pull(task_ids="extract_task")
    df = pd.DataFrame(data)

    df.dropna(inplace=True)
    df["total_amount"] = df["quantity"] * df["price"]

    print("Transformation successful")
    return df.to_dict()


def load(ti):
    data = ti.xcom_pull(task_ids="transform_task")
    df = pd.DataFrame(data)

    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM retail_sales")

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO retail_sales 
            (order_id, customer_name, product_name, quantity, price, total_amount)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            int(row["order_id"]),
            row["customer_name"],
            row["product_name"],
            int(row["quantity"]),
            float(row["price"]),
            float(row["total_amount"])
        ))

    conn.commit()
    cursor.close()
    conn.close()

    print("Load successful")


def aggregate():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*), SUM(total_amount) FROM retail_sales")
    result = cursor.fetchone()

    cursor.execute("DELETE FROM sales_summary")

    cursor.execute("""
        INSERT INTO sales_summary (total_orders, total_revenue)
        VALUES (%s, %s)
    """, result)

    conn.commit()
    cursor.close()
    conn.close()

    print("Aggregation successful")
