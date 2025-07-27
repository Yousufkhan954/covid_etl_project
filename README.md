# COVID-19 ETL Data Pipeline

A simple ETL project in Python that reads COVID-19 data from a CSV file, processes it using pandas, and loads it into a MySQL database.

## Tools Used
- Python (pandas, mysql-connector)
- MySQL
- SQL

## Features
- Data cleaning and transformation
- Schema creation and data loading
- SQL queries for reporting (total cases, death rate)

## Sample Query
```sql
SELECT country, SUM(confirmed) FROM covid_stats GROUP BY country;
