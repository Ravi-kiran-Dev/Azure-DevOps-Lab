# terraform/k8s.tf
resource "helm_release" "strimzi" {
  name       = "strimzi"
  repository = "https://strimzi.io/charts/"
  chart      = "strimzi-kafka-operator"
  version    = "0.40.0"

  namespace        = "kafka"
  create_namespace = true
}

resource "kubernetes_manifest" "kafka_cluster" {
  manifest = {
    "apiVersion" = "kafka.strimzi.io/v1beta2"
    "kind"       = "Kafka"
    "metadata" = {
      "name"      = "my-cluster"
      "namespace" = "kafka"
    }
    "spec" = {
      "kafka" = {
        "version"   = "3.7.0",
        "replicas"  = 1,
        "listeners" = [
          { "name" = "plain", "port" = 9092, "type" = "internal", "tls" = false },
          { "name" = "external", "port" = 9094, "type" = "nodeport", "tls" = false, "configuration" = {
            "bootstrap" = {
              "nodePort" = 32094
            },
            "brokers" = [
              {
            "broker" = 0,
            "advertisedHost" = "localhost",
            "advertisedPort" = 9094
          }
        ]
          }
          }
        ],
        "config" = {
          "offsets.topic.replication.factor" = 1,
          "transaction.state.log.replication.factor" = 1,
          "log.retention.hours" = 168
        },
        "storage" = { "type" = "ephemeral" }
      },
      "zookeeper" = {
        "replicas" = 1,
        "storage" = { "type" = "ephemeral" }
      },
      "entityOperator" = {
        "topicOperator" = {},
        "userOperator"  = {}
      }
    }
  }

  depends_on = [helm_release.strimzi]
}