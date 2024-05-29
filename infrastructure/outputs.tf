output "region" {
  value       = var.region
  description = "GCP Region"
}

output "project_id" {
  value       = var.project_id
  description = "GCP Project ID"
}

output "kubernetes_cluster_name" {
  value       = google_container_cluster.hackathon.name
  description = "GKE Cluster Name"
}

output "kubernetes_cluster_host" {
  value       = google_container_cluster.hackathon.endpoint
  description = "GKE Cluster Host"
}
