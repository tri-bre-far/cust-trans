variable "project_id" {
  description = "GCP project ID"
  type        = string
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "europe-west1" # Belgium region
}

variable "dataflow_sa" {
  description = "Service account email for Dataflow jobs"
  type        = string
}
