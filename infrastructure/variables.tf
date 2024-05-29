variable "project_id" {
  description = "project id"
}

variable "region" {
  description = "region"
}

variable "gke_num_nodes" {
  description = "number of gke nodes"
}

variable "gke_machine_type" {
  description = "gke nodes machine type"
}

variable "vpc_ip_range" {
  description = "main vpc ip range"
}

variable "gke_pod_ip_range" {
  description = "ip range for gke pods"
}

variable "gke_service_ip_range" {
  description = "ip range for gke services"
}

variable "gke_master_ip_range" {
  description = "gke master ip range"
}
