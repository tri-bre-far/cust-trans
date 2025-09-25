from faker import Faker
import csv
import random

fake = Faker()
num_customers = 1000  # Adjust as needed
customers = []

def maybe_missing(value, probability=0.1):
    return value if random.random() > probability else ""

def dirty_email(email):
    if random.random() < 0.05:
        return email.replace("@", "")  # malformed
    return email

def dirty_age(age):
    if random.random() < 0.05:
        return "unknown"  # invalid type
    return age

with open("customers.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["customer_id", "name", "email", "age"])

    for customer_id in range(1, num_customers + 1):
        if random.random() < 0.05 and customers:  # 5% chance of duplicate
            writer.writerow(random.choice(customers))
            continue

        name = maybe_missing(fake.name())
        email = maybe_missing(dirty_email(fake.email().lower()))
        age = maybe_missing(dirty_age(random.randint(18, 75)))

        row = [customer_id, name, email, age]
        customers.append(row)
        writer.writerow(row)

print(f"✅ Generated customers.csv with {num_customers} rows (including missing and duplicate data)")