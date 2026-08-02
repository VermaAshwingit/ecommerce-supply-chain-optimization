import pandas as pd
import os

print("1. Loading datasets...")
# Using relative paths since your CSVs are in the 'data' folder
orders = pd.read_csv('data/olist_orders_dataset.csv')
customers = pd.read_csv('data/olist_customers_dataset.csv')
items = pd.read_csv('data/olist_order_items_dataset.csv')

print("2. Converting timestamps (this might take a few seconds)...")
time_columns = ['order_purchase_timestamp', 'order_delivered_customer_date', 'order_estimated_delivery_date']
for col in time_columns:
    orders[col] = pd.to_datetime(orders[col])

print("3. Calculating delivery delays...")
# Positive number = Days Late. Negative number = Days Early.
orders['delivery_delay_days'] = (orders['order_delivered_customer_date'] - orders['order_estimated_delivery_date']).dt.days

print("4. Filtering for delayed deliveries...")
# Keep only delivered orders that arrived after the estimated date
late_orders = orders[(orders['order_status'] == 'delivered') & (orders['delivery_delay_days'] > 0)]

print("5. Merging tables to find location and cost data...")
merged_df = late_orders.merge(customers, on='customer_id', how='left')
final_df = merged_df.merge(items, on='order_id', how='left')

print(f"Success! Found {len(final_df)} late items.")

print("6. Exporting to a new CSV for SQL and Power BI...")
final_df.to_csv('data/cleaned_late_deliveries.csv', index=False)
print("Done! Check your 'data' folder for 'cleaned_late_deliveries.csv'.")