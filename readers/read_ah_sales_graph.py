import duckdb
import matplotlib.pyplot as plt
import pandas as pd

# Create DuckDB database connection
conn = duckdb.connect('pharma_sales/sales_db.duckdb')

# Execute query to retrieve data
result = conn.execute("SELECT * FROM public.antihistamine_sales_by_month").fetchdf()

# Close the connection
conn.close()

# Verify the data (optional)
print(result)

# Plotting the data
plt.figure(figsize=(10, 6))

# Assume 'month' and 'sales_amount' are columns in the dataset
plt.plot(result['Month'], result['antihitamine_sales'], marker='o', color='b', linestyle='-', label='Sales')

# Customize the plot
plt.title('Antihistamine Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
