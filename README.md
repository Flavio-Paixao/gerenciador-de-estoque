# 📦 Gerenciador de Estoque — Django + AWS RDS + CloudWatch

> Sistema completo de controle de estoque com API REST, banco PostgreSQL gerenciado no AWS RDS, servidor EC2 criado via Terraform e monitoramento com CloudWatch.

🔗 **[Ver ao vivo](http://15.229.54.25:8000)**  
📁 **[Repositório](https://github.com/Flavio-Paixao/gerenciador-de-estoque)**

---

## 🏗️ Arquitetura

```
Frontend (S3) → Django API (EC2) → PostgreSQL (RDS)
                      ↓
               CloudWatch (CPU + Alertas SNS)
```

---

## ☁️ Recursos AWS Utilizados

| Serviço | Função |
|---|---|
| **EC2 t3.micro** | Servidor Ubuntu 22.04 rodando a API Django |
| **AWS RDS** | PostgreSQL gerenciado com backup automático |
| **Terraform** | Infraestrutura criada como código |
| **CloudWatch** | Monitoramento de CPU com alertas por email |
| **SNS** | Notificações por email quando CPU > 80% |
| **Security Group** | Firewall configurado via Terraform |
| **Elastic IP** | IP fixo para a instância EC2 |
| **systemd** | Mantém a API sempre ativa após reboots |

---

## 📁 Estrutura do Projeto

```
gerenciador-de-estoque/
├── app/
│   ├── config/          # Configurações Django
│   ├── produtos/        # App de produtos e categorias
│   ├── movimentacoes/   # App de movimentações de estoque
│   └── templates/       # Frontend HTML
└── terraform/
    ├── main.tf          # EC2, Security Group, Elastic IP
    ├── providers.tf     # Provider AWS
    └── outputs.tf       # IPs e URLs gerados
```

---

## 🚀 Funcionalidades

**Produtos:**
- Cadastro com código, nome, descrição, preço e quantidade
- Quantidade mínima com alerta de estoque baixo
- Filtro por categoria e busca por nome

**Categorias:**
- CRUD completo de categorias de produtos

**Movimentações:**
- Registro de entradas e saídas de estoque
- Atualização automática da quantidade do produto
- Histórico completo de movimentações

**Dashboard:**
- Cards com totais de produtos, categorias e movimentações
- Alerta visual de produtos com estoque baixo

---

## 🛠️ Como rodar localmente

### Pré-requisitos
- Python 3.10+
- PostgreSQL ou AWS RDS configurado

### Instalação

```bash
git clone https://github.com/Flavio-Paixao/gerenciador-de-estoque.git
cd gerenciador-de-estoque/app
python -m venv venv
source venv/Scripts/activate  # Windows
pip install django djangorestframework drf-spectacular psycopg2-binary gunicorn django-cors-headers django-filter
```

### Configurar banco no settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'seu-endpoint.rds.amazonaws.com',
        'PORT': '5432',
    }
}
```

### Rodar

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse: `http://localhost:8000`

---

## 🏗️ Infraestrutura com Terraform

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

**Outputs:**
```
api_url    = "http://SEU_IP:8000"
public_ip  = "SEU_IP"
```

---

## 📊 Monitoramento CloudWatch

- **Dashboard:** `estoque-dashboard` com métricas de CPU
- **Alarme:** `estoque-cpu-alta` — notifica via email quando CPU > 80%
- **SNS Topic:** `estoque-alertas`

---

## 👨‍💻 Sobre

**Flávio da Paixão Nunes** — Desenvolvedor Backend Python | AWS Cloud  
Estudante de Engenharia de Software (Ampli/Anhanguera) — 2º ano  
Santos, São Paulo - SP

[![LinkedIn](https://img.shields.io/badge/LinkedIn-flaviopx-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/flaviopx)
[![GitHub](https://img.shields.io/badge/GitHub-Flavio--Paixao-black?style=flat&logo=github)](https://github.com/Flavio-Paixao)
[![Portfolio](https://img.shields.io/badge/Portf%C3%B3lio-fpx.Dev-orange?style=flat&logo=amazonaws)](https://projeto-aws-681892816208-sa-east-1-an.s3.sa-east-1.amazonaws.com/index.html)

---

## 🚀 Stack

![Django](https://img.shields.io/badge/Django-REST-green?style=flat&logo=django)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-RDS-blue?style=flat&logo=postgresql)
![Terraform](https://img.shields.io/badge/Terraform-IaC-purple?style=flat&logo=terraform)
![AWS EC2](https://img.shields.io/badge/EC2-Server-orange?style=flat&logo=amazonaws)
![CloudWatch](https://img.shields.io/badge/CloudWatch-Monitoring-orange?style=flat&logo=amazonaws)
![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python)
