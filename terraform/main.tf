# AMI Ubuntu 22.04
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

# Security Group
resource "aws_security_group" "estoque_sg" {
  name        = "estoque-sg"
  description = "Security Group Gerenciador de Estoque"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name    = "estoque-sg"
    Project = "gerenciador-de-estoque"
  }
}

# Key Pair
resource "aws_key_pair" "estoque_key" {
  key_name   = "estoque-key"
  public_key = file("~/.ssh/terraform-key.pub")
}

# EC2
resource "aws_instance" "estoque_server" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t3.micro"
  key_name               = aws_key_pair.estoque_key.key_name
  vpc_security_group_ids = [aws_security_group.estoque_sg.id]

  tags = {
    Name    = "estoque-server"
    Project = "gerenciador-de-estoque"
  }
}

# Elastic IP
resource "aws_eip" "estoque_eip" {
  instance = aws_instance.estoque_server.id
  domain   = "vpc"

  tags = {
    Name    = "estoque-eip"
    Project = "gerenciador-de-estoque"
  }
}