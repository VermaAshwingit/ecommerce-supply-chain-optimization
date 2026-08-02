import pandas as pd
import sqlite3

print("1. Loading the cleaned CSV...")
# Load the CSV we just created
df = pd.read_csv('data/cleaned_late_deliveries.csv')

print("2. Connecting to SQLite database...")
# This will automatically create a file named 'supply_chain.db' in your folder
conn = sqlite3.connect('supply_chain.db')

print("3. Pushing data into the database...")
# Push the dataframe into a SQL table named 'late_deliveries'
df.to_sql('late_deliveries', conn, if_exists='replace', index=False)

print("Success! The data is now inside the 'supply_chain.db' database.")

# Close the connection
conn.close()