CREATE OR REPLACE TABLE customer_analytics.monthly_spend
PARTITION BY month
CLUSTER BY customer_id AS
SELECT
  customer_id,
  FORMAT_TIMESTAMP('%Y-%m', transaction_date) AS month,
  SUM(amount) AS total_spend,
  AVG(amount) AS avg_spend
FROM customer_analytics.transactions
GROUP BY customer_id, month;