provider "aws" {
  region = "us-east-1"
}

resource "aws_iam_user" "my_new_user" {
  name = "huseyin-terraform-${var.environment}"
}