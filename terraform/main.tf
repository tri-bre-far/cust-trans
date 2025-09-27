terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = 'data-engineer-task-python'
  region  = 'europe-west1'
}

resource "google_storage_bucket" "data_bucket" {
  name     = "customer-transactions-01"
  location = "US"
}

resource "google_bigquery_dataset" "analytics" {
  dataset_id = "customer_analytics"
  location   = "EU"
  description = "Dataset for customer transaction analytics"
}

resource "google_project_iam_member" "dataflow_worker" {
  project = 'data-engineer-task-python'
  role    = "roles/dataflow.admin"
  member  = "321240239901-compute@developer.gserviceaccount.com"
}

resource "google_project_iam_member" "bigquery_user" {
  project = 'data-engineer-task-python'
  role    = "roles/bigquery.dataEditor"
  member  = "321240239901-compute@developer.gserviceaccount.com"
}


resource "google_project_iam_member" "storage_object_user" {
  project = 'data-engineer-task-python'
  role    = "roles/storage.objectAdmin"
  member  = "321240239901-compute@developer.gserviceaccount.com"
}
