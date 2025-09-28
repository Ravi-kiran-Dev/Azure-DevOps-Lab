# Azure Kafka DevOps Lab

A self-driven project demonstrating modern cloud-native infrastructure on **Microsoft Azure**.

## 🛠️ Tech Stack
- **Cloud**: Azure (AKS, Resource Groups)
- **IaC**: Terraform
- **Messaging**: Apache Kafka (via Strimzi on Kubernetes)
- **CI/CD**: GitHub Actions (planned)
- **Monitoring**: Prometheus + Grafana (planned)

## 🚀 What It Does
1. **Terraform** provisions AKS cluster (`Standard_B2s` VMs — free on Dev/Test)
2. **Strimzi Operator** deploys Kafka cluster
3. Kafka cluster runs with **1 Kafka + 1 Zookeeper replica** (lab-optimized)

## 💡 Why I Built This
With 9 years in Azure support, I’ve seen how fragile manual systems can be. This lab is my step toward **building resilient, automated platforms**—not just fixing them.

> "I learn by doing. This is how I prepare for roles like yours."

## 🖼️ Deployment Proof

| Azure Infra | AKS Nodes |
|-------------|-----------|
| ![Azure](screenshots/01-terraform-apply-success.png) | ![Nodes](screenshots/02-kubectl-nodes.png) |

| Strimzi CRDs | Kafka Pods |
|--------------|------------|
| ![CRDs](screenshots/03-strimzi-crds.png) | ![Pods](screenshots/04-kafka-pods.png) |

| Kafka CR | Azure Portal (Main RG) |
|----------|------------------------|
| ![CR](screenshots/05-kafka-cr.png) | ![Portal](screenshots/06a-azure-main-rg.png) |

| Azure Portal (Node RG) |
|------------------------|
| ![Node RG](screenshots/06b-azure-node-rg.png) |

> 💡 **Note**:  
> - `kafka-devops-rg`: Terraform-managed (control plane)  
> - `MC_kafka-devops-rg_lab-aks_eastus`: Auto-created by Azure (worker nodes)

## ▶️ How to Run (For Future Reference)
1. `terraform apply -target=azurerm_resource_group.main -target=azurerm_kubernetes_cluster.main`
2. `az aks get-credentials --name lab-aks --resource-group kafka-devops-rg`
3. `terraform apply`
4. `kubectl get pods -n kafka`

> ⚠️ **All resources were destroyed after validation to maintain $0 cost** on Visual Studio Enterprise Dev/Test subscription.