## Extra things to do

As with any project, there is always room for numerous add-ons and improvements. Some of them are listed here.

### Preview environments clean-up

To avoid accumulating unused preview environments and wasting infrastructure resources, this project requires a script to delete environments older than one week. You can create a regular clean-up job with this script. The clean-up process can be improved with checks and notifications to developers. By clicking a link in the notification messages, developers can mark environments as not to be deleted for the next week.

### Managed DNS

We aim to use Google Cloud DNS and configure it to automatically update DNS A records for a Google Cloud Load Balancer. This will ensure that our subdomain always directs traffic to the correct load balancers used for ingress traffic to preview environments.

### Monitoring

Extend current GCP monitoring and logging by integrating OpenTelemetry for distributed tracing and metrics, and Grafana for advanced visualization. Deploy a tracing backend like Jaeger to enhance observability, allowing for better performance monitoring, trace analysis, and insightful dashboards. This setup will improve debugging and optimization of preview environments.

### Security

Enhance security by implementing Google Cloud Secret Manager for securely storing and managing tokens, passwords, and keys. We aim to avoid any hardcoded secrets or storing sensitive information in configuration files. Additionally, we will enforce least privilege access using IAM roles and permissions.

### Containerization

Improve deployment efficiency, security, and infrastructure simplicity by adopting Google Cloud Run. This approach can significantly reduce the manual steps required for installing an application and setting up the application environment.

### Scaling

Implement autoscaling in the existing GKE cluster to optimize resource usage. Enabling node pool autoscaling adjusts node numbers dynamically based on workload needs, ensuring efficient resource allocation and cost savings. Additionally, cluster autoscaling scales the entire cluster based on overall resource usage, enabling the creation of more preview environments automatically.

### Costs

Implementing robust cost tracking and alerting to avoid overspending costs with node pool autoscaling.
