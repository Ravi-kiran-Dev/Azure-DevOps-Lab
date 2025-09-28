variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "kafka-devops-rg"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "East US"
}

variable "prefix" {
  description = "Naming prefix for resources"
  type        = string
  default     = "lab"
}