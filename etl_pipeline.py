import pandas as pd
import mysql.connector

# Load CSV
df = pd.read_csv('covid_data.csv')

# Data Cleaning
df['Date'] = pd.to_datetime(df['Date'])
df.fillna(0, inplace=True)

# Connect to MySQL (edit these with your real credentials)
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="covid_db"
)
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS covid_stats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    country VARCHAR(50),
    confirmed INT,
    deaths INT,
    recovered INT
)
""")

# Insert Rows
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO covid_stats (date, country, confirmed, deaths, recovered)
        VALUES (%s, %s, %s, %s, %s)
    """, (row['Date'].date(), row['Country'], int(row['Confirmed']), int(row['Deaths']), int(row['Recovered'])))

conn.commit()
conn.close()
