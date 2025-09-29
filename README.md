# Azure Event-Driven Architecture Lab

A production-grade event streaming platform built on **Microsoft Azure** demonstrating **real-time payment processing with fraud detection**.

## 🎯 Why I Built This
With 9 years in Azure support, I've seen how fragile manual systems can be. This lab demonstrates my transition from **reacting to outages** to **engineering resilient, automated platforms** using modern DevOps practices.

## 🛠️ Technologies Implemented
| Category | Technologies |
|----------|-------------|
| **Cloud Infrastructure** | Azure, Terraform, AKS |
| **Event Streaming** | Apache Kafka (Strimzi), Kafka Producer/Consumer |
| **Applications** | Python (Payment Producer, Fraud Detection Consumer) |
| **Observability** | kubectl, Kafka CLI tools |
| **Security & Networking** | Internal/External Kafka listeners, TLS-ready design |

## 🚀 End-to-End Workflow
1. **Infrastructure**: Terraform provisions AKS cluster with B2s VMs (free tier eligible)
2. **Kafka**: Strimzi operator deploys Kafka with external listeners for local development
3. **Payment Producer**: Sends realistic payment events to `user-payments` topic
4. **Fraud Detection**: Real-time consumer flags high-value transactions
5. **Validation**: Verified with Kafka console consumer and Azure Portal

## 🖼️ Deployment Proof

### Azure Infrastructure
| Resource Group | AKS Nodes |
|----------------|-----------|
| ![Azure RG](Screenshots/01-terraform-apply-success.png) | ![Nodes](Screenshots/02-kubectl-nodes.png) |

### Kafka Deployment
| Strimzi CRDs | Kafka Pods | Kafka Custom Resource |
|--------------|------------|----------------------|
| ![CRDs](Screenshots/03-strimzi-crds.png) | ![Pods](Screenshots/04-kafka-pods.png) | ![CR](Screenshots/05-kafka-cr.png) |

### Azure Portal
| Main Resource Group | Node Resource Group |
|---------------------|---------------------|
| ![Main RG](Screenshots/06a-azure-main-rg.png) | ![Node RG](Screenshots/06b-azure-node-rg.png) |

### Payment Processing Pipeline
| Payment Producer | Fraud Detection | Raw Kafka Messages |
|------------------|-----------------|-------------------|
| ![Producer](Screenshots/07-payment-producer.png) | ![Fraud](Screenshots/08-fraud-consumer.png) | ![Raw](Screenshots/09-kafka-raw.png) |

## 💡 Key Technical Decisions
- **Cost Optimization**: Used B2s VMs (free on Dev/Test subscriptions)
- **External Access**: Configured Kafka advertised listeners for local development
- **Resilience**: Implemented proper error handling and timeouts in Python clients
- **Validation**: Verified every component before proceeding to next step

## ▶️ How to Reproduce
```bash
# 1. Deploy Azure infrastructure
terraform apply -target=azurerm_resource_group.main -target=azurerm_kubernetes_cluster.main

# 2. Configure kubectl
az aks get-credentials --name lab-aks --resource-group kafka-devops-rg

# 3. Deploy Kafka
terraform apply

# 4. Port-forward for local access
kubectl port-forward -n kafka svc/my-cluster-kafka-external-bootstrap 9094:9094

# 5. Run producer/consumer
python apps/payment-producer/payment_producer.py
python apps/fraud-consumer/fraud_consumer.py