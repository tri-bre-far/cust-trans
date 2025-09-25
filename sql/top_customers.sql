CREATE OR REPLACE TABLE data-engineer-task-python.customer_analytics.top_customers
CLUSTER BY customer_id AS
SELECT
  customer_id,
  SUM(amount) AS lifetime_spend
FROM
  data-engineer-task-python.customer_analytics.transactions_deduped
GROUP BY
  customer_id
QUALIFY
  PERCENT_RANK() OVER (ORDER BY SUM(amount) DESC) <= 0.05;
