CREATE OR REPLACE TABLE data-engineer-task-python.customer_analytics.monthly_spend
PARTITION BY DATE_TRUNC(transaction_date, MONTH)
CLUSTER BY customer_id AS
SELECT
  customer_id,
  FORMAT_DATE('%Y-%m', transaction_date) AS month,
  SUM(amount) AS total_spend,
  AVG(amount) AS avg_spend,
  transaction_date
FROM
  data-engineer-task-python.customer_analytics.transactions_deduped
GROUP BY
  customer_id, month, transaction_date;
