import pandas as pd
import sqlite3

print("1. Connecting to the database...")
conn = sqlite3.connect('supply_chain.db')

print("2. Running the SQL query...")
# We use Pandas to run the exact same SQL query you just tested in VS Code
query = """
SELECT 
    customer_state,
    COUNT(order_id) AS total_late_orders,
    ROUND(AVG(delivery_delay_days), 2) AS avg_days_late,
    SUM(freight_value) AS total_shipping_revenue_at_risk
FROM 
    late_deliveries
GROUP BY 
    customer_state
ORDER BY 
    total_late_orders DESC
LIMIT 10;
"""

# Store the query results into a Pandas dataframe
results_df = pd.read_sql(query, conn)

print("3. Exporting the results to a file...")
# Save it as a CSV file in your data folder
results_df.to_csv('data/top_10_late_states.csv', index=False)

print("Success! You can now open 'top_10_late_states.csv' in Excel.")
conn.close()