provider "aws" {
  region = var.region
    access_key = "AKIAXUHDO44OCYFM6D7A"
    secret_key = "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"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>3.0"
    }
  }
}