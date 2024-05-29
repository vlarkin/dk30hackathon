# Create a VM instance with 10GB boot disk
resource "google_compute_instance" "ubuntu_vm" {
  name         = "ubuntu-hackathon1"
  machine_type = "e2-small"
  zone         = "europe-west1-b"

  boot_disk {
    initialize_params {
      image = "ubuntu-2204-lts"
      size  = 10
    }
  }

  network_interface {
    network = google_compute_network.main.name
    access_config {}
  }
}
