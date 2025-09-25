CREATE OR REPLACE TABLE customer_analytics.top_customers
CLUSTER BY customer_id AS
SELECT
  customer_id,
  SUM(amount) AS lifetime_spend
FROM customer_analytics.transactions
GROUP BY customer_id;