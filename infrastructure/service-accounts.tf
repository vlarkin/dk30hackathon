
resource "google_service_account" "kubernetes" {
  account_id = "kubernetes"
}

resource "google_storage_bucket_iam_member" "kubernetes" {
  bucket  = "artifacts.${var.project_id}.appspot.com"
  role    = "roles/storage.objectViewer"
  member  = "serviceAccount:${google_service_account.kubernetes.email}"
}
