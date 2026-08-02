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