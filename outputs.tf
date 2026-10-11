output "instance_id" {
  description = "ID of the AI EC2 instance"
  value       = aws_instance.ai_server.id
}

output "instance_type" {
  description = "EC2 instance type"
  value       = aws_instance.ai_server.instance_type
}

output "public_ip" {
  description = "Public IP of the AI EC2 instance"
  value       = aws_instance.ai_server.public_ip
}
