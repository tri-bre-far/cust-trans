from faker import Faker
import csv
import random
from datetime import datetime, timedelta

fake = Faker()
num_transactions = 5000  # Adjust as needed
customer_ids = list(range(1, 1001))  # Match with customers.csv

transaction_types = ['purchase', 'refund', 'withdrawal', 'deposit']

def random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def maybe_missing(value, probability=0.05):
    return value if random.random() > probability else ""

with open("transactions.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "customer_id", "transaction_date", "amount", "transaction_type"])

    transactions = []
    for transaction_id in range(1, num_transactions + 1):
        if random.random() < 0.03 and transactions:  # 3% chance of duplicate
            writer.writerow(random.choice(transactions))
            continue

        customer_id = random.choice(customer_ids)
        transaction_date = random_date(datetime(2022, 1, 1), datetime(2025, 9, 1)).strftime("%Y-%m-%d %H:%M:%S")
        amount = round(random.uniform(5.0, 500.0), 2)
        transaction_type = random.choice(transaction_types)

        # Simulate missing or dirty data
        customer_id = maybe_missing(customer_id)
        transaction_date = maybe_missing(transaction_date)
        amount = maybe_missing(amount)
        transaction_type = maybe_missing(transaction_type)

        row = [transaction_id, customer_id, transaction_date, amount, transaction_type]
        transactions.append(row)
        writer.writerow(row)

print(f"✅ Generated transactions.csv with {num_transactions} rows (including missing and duplicate data)")