# Customer Transactions 
This project prototypes a secure, scalable data pipeline using Google Cloud. It ingests customer and transaction data, transforms it using Apache Beam, and exposes analytics-ready views in BigQuery.

## Features
- Data ingestion from GCS to BigQuery
- Schema validation and cleansing
- Monthly and lifetime spend analytics
- Modular Python code with tests
- CI/CD with GitHub Actions

## 🏗️ Architecture Overview

cust-trans/
├── pipeline/                  # Python transformation logic
│   ├── transforms.py
│   └── test_transforms.py
├── terraform/                 # Terraform infrastructure setup
│   ├── main.tf                # Core resources (GCS, BigQuery, IAM)
│   ├── variables.tf           # Input variables
│   └──  outputs.tf            # Output values
├── data/                     # data used for tables
│   ├── cutomers.csv          #dummy customer profile data
│   └── transactions.csv      #dummy raw transactions logs
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── python-ci.yml

## 🚀 Setup Instructions
1. Enable GCP APIs: Dataflow, BigQuery, Storage
2. Run `terraform apply` to provision infra
3. Upload CSVs to GCS
4. Execute `beam_custmers_pipeline.py` & `beam_transactions_pipeline.py`via Dataflow
5. Create materialized tables in BigQuery

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
