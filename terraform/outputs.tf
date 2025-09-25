output "bucket_name" {
  value = google_storage_bucket.raw_data.name
}

output "dataset_id" {
  value = google_bigquery_dataset.analytics.dataset_id
}
