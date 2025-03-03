import duckdb

# create Duck DB database from CSV files
conn = duckdb.connect('pharma_sales/sales_db.duckdb')

# verify that the data has been loaded
result = conn.execute("SELECT * FROM public.my_first_dbt_model LIMIT 1").fetchall()
print(result)

# Close the connection
conn.close()