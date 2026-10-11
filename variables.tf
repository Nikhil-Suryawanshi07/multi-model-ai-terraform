variable "aws_region" {
  description = "AWS region for the AI deployment"
  type        = string
  default     = "us-east-1"
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
  default     = "ami-0b6d9d3d33ba97d99"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "c7i-flex.xlarge"
}

variable "subnet_id" {
  description = "Existing subnet ID"
  type        = string
  default     = "subnet-0cc0a287edd69354d"
}

variable "security_group_id" {
  description = "Existing security group ID"
  type        = string
  default     = "sg-06576e58c4c658da4"
}

variable "key_name" {
  description = "Existing EC2 key pair name"
  type        = string
  default     = "A"
}

variable "iam_instance_profile" {
  description = "Existing EC2 IAM instance profile"
  type        = string
  default     = "ai_model"
}
