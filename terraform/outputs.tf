output "instance_id" {
  description = "ID da instância EC2"
  value       = aws_instance.estoque_server.id
}

output "public_ip" {
  description = "IP público da instância"
  value       = aws_eip.estoque_eip.public_ip
}

output "api_url" {
  description = "URL da API"
  value       = "http://${aws_eip.estoque_eip.public_ip}:8000"
}

output "security_group_id" {
  description = "ID do Security Group"
  value       = aws_security_group.estoque_sg.id
}