resource "google_container_cluster" "hackathon" {
  name                     = "hackathon"
  location                 = "${var.region}"
  remove_default_node_pool = false
  initial_node_count       = 1
  network                  = google_compute_network.main.self_link
  subnetwork               = google_compute_subnetwork.private.self_link
  networking_mode          = "VPC_NATIVE"

  # Optional, if you want multi-zonal cluster
  node_locations = [
    "${var.region}-b",
    "${var.region}-c",
    "${var.region}-d"
  ]

  node_config {
    preemptible  = true
    machine_type = var.gke_machine_type
    disk_size_gb = 50
    disk_type = "pd-standard"

    labels = {
      role = "general"
    }

    service_account = google_service_account.kubernetes.email

    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }

  addons_config {
    http_load_balancing {
      disabled = true
    }
    horizontal_pod_autoscaling {
      disabled = false
    }
  }

  release_channel {
    channel = "REGULAR"
  }

  ip_allocation_policy {
    cluster_secondary_range_name  = "k8s-pod-range"
    services_secondary_range_name = "k8s-service-range"
  }

  private_cluster_config {
    enable_private_nodes    = true
    enable_private_endpoint = false
    master_ipv4_cidr_block  = var.gke_master_ip_range
  }
}
