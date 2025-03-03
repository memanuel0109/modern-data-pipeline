import duckdb

# create Duck DB database from CSV files for DBT model
conn = duckdb.connect('pharma_sales/sales_db.duckdb')

# create tables table
conn.execute("""
CREATE OR REPLACE TABLE sales_daily (
    datum VARCHAR(20),
    M01AB FLOAT,
    M01AE FLOAT,
    N02BA FLOAT,
    N02BE FLOAT,
    N05B FLOAT,
    N05C FLOAT,
    R03 FLOAT,
    R06 FLOAT,
    Year INTEGER,
    Month INTEGER,
    Hour INTEGER,
    Weekday_name CHAR(10)
);
""")

# create hourly table
conn.execute("""
CREATE OR REPLACE TABLE sales_hourly (
    datum VARCHAR(20),
    M01AB FLOAT,
    M01AE FLOAT,
    N02BA FLOAT,
    N02BE FLOAT,
    N05B FLOAT,
    N05C FLOAT,
    R03 FLOAT,
    R06 FLOAT,
    Year INTEGER,
    Month INTEGER,
    Hour INTEGER,
    Weekday_name CHAR(10)
);
""")

# create monthly table
conn.execute("""
CREATE OR REPLACE TABLE sales_monthly (
    datum VARCHAR(20),
    M01AB FLOAT,
    M01AE FLOAT,
    N02BA FLOAT,
    N02BE FLOAT,
    N05B FLOAT,
    N05C FLOAT,
    R03 FLOAT,
    R06 FLOAT
);
""")

# create weekly table
conn.execute("""
CREATE OR REPLACE TABLE sales_weekly (
    datum VARCHAR(20),
    M01AB FLOAT,
    M01AE FLOAT,
    N02BA FLOAT,
    N02BE FLOAT,
    N05B FLOAT,
    N05C FLOAT,
    R03 FLOAT,
    R06 FLOAT
);
""")

# import data from CSV files into DuckDB table
conn.execute("""
    COPY sales_daily FROM './datasets/salesdaily.csv' (DELIMITER ',', HEADER TRUE);
    COPY sales_hourly FROM './datasets/saleshourly.csv' (DELIMITER ',', HEADER TRUE);
    COPY sales_monthly FROM './datasets/salesmonthly.csv' (DELIMITER ',', HEADER TRUE);
    COPY sales_weekly FROM './datasets/salesweekly.csv' (DELIMITER ',', HEADER TRUE);
""")

results = []

# verify that the data has been loaded
for table in ["sales_daily", "sales_hourly", "sales_monthly", "sales_weekly"]:
    result = conn.execute(f"SELECT * FROM {table} LIMIT 1").fetchall()
    print(result)

# close the connection
conn.close()