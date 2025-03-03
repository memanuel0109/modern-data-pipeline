import duckdb

# create Duck DB database from CSV files
conn = duckdb.connect('pharma_sales/sales_db.duckdb')

# verify that the data has been loaded
result = conn.execute("SELECT * FROM public.records_by_doy").fetchall()
print(result)

# Close the connection
conn.close()