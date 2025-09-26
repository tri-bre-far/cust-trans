# Customer Transactions 
This project prototypes a secure, scalable data pipeline using Google Cloud. It ingests customer and transaction data, transforms it using Apache Beam, and exposes analytics-ready views in BigQuery.

## Features
- Data ingestion from GCS to BigQuery
- Schema validation and cleansing
- Monthly and lifetime spend analytics
- Modular Python code with tests
- CI/CD with GitHub Actions

## 🏗️ Architecture Overview
```
cust-trans/
├── pipeline/                  # Python transformation logic
│   ├── transforms.py
│   └── test_transforms.py
├── terraform/                    # Terraform infrastructure setup
│   ├── main.tf                   # Core resources (GCS, BigQuery, IAM)
│   ├── variables.tf              # Input variables
│   └──  outputs.tf               # Output values
├── data/                         # data used for tables
│   ├── cutomers.csv              
│   └── transactions.csv         
├── sql/                          # materialized tables
│   ├── top_customers.sql         #top 5% customers
│   └── monthly_spend.sql         #total and avg monthly spend per customer
├── python/                       # other python scripts used
│   ├── generate_customers.py     
│   ├── generate_transactions.py
│   ├── beam_customers_pipeline.py
│   └── beam_transactions_pipeline.py
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── python-ci.yml
```

## 🚀 Setup Instructions
1. Enable GCP APIs: Dataflow, BigQuery, Storage
2. Generate & Upload CSVs to GCS via the `generate_transactions.py` & `generate_customers.py`
3. Test `beam_customers_pipeline.py` & `beam_transactions_pipeline.py` by running:  python beam_customers_pipeline.py --runner DirectRunner
4. Execute `beam_customers_pipeline.py` & `beam_transactions_pipeline.py`via Dataflow to create a modular beam pipeline which will package code, upload to the staging bucket & generate a dataflow job
5. Apply partitioning on transaction date & clustering on customer_id to the transactions table in BigQuery
6. Create materialized tables in BigQuery using top_customers.sql & monthly_spend.sql
7. test test_transforms.py using pytest
8. Run `terraform apply` to provision infra
9. Enable Github Actions

### 🔐 GCP Permissions
Ensure the following APIs are enabled:
- Cloud Storage
- Dataflow
- BigQuery
- IAM

Create a service account with roles:
- `roles/dataflow.worker`
- `roles/bigquery.dataEditor`
- `roles/storage.objectAdmin`

### ⚙️ Terraform Deployment
```bash
cd terraform
terraform init
terraform apply
```

## 📌 Assumptions
- CSVs are UTF-8 encoded and contain headers
- Timestamps are in UTC
- Email addresses require normalization
- Nulls and type mismatches are handled in the pipeline

## 🔮 Future Improvements
- Terraform, need to test once resolve issues
- Need to fix the errors in test_transforms.py
- Consider BigQuery table-level encryption if sensitive fields are involved  
- Add dbt for modular SQL modelLing
- Integrate Cloud Composer for orchestration
- Implement data quality checks
- Add anomaly detection for spend patterns
- Enable streaming ingestion for real-time analytics

