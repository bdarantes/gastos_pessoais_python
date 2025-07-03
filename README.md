# 💰 Controle de Gastos Pessoais - Terminal App

Um aplicativo simples de terminal, feito em Python, para ajudar no controle de gastos pessoais. Utiliza banco de dados SQLite3 para armazenar as informações de forma local e persistente.

## 📌 Funcionalidades

- Adicionar gastos com descrição e valor
- Listar todos os gastos registrados


## ⚙️ Tecnologias Utilizadas

- Python 3.x
- SQLite3 (banco de dados embutido)
- Interface via terminal

## 📁 Estrutura do Projeto

```
gastos_pessoais/
├── __init__.py
├── db.py
├── controle_de_gastos.py
├── requirements.txt
└── README.md

```


## 🚀 Como Executar

1. Clone o repositório:
```bash
git clone git@github.com:bdarantes/gastos_pessoais_python.git
cd gastos_pessoais

    (Opcional) Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

    Execute o app:

python controle_de_gastos.py

🗃️ Banco de Dados

O banco de dados será criado automaticamente como um arquivo local gastos.db na primeira execução.
📌 Exemplo de Uso

Bem-vindo ao Controle de Gastos
[1] Adicionar Gasto
[2] Listar Gastos
[3] Sair

📝 Licença

Este projeto está em desenvolvimento e ainda não possui uma licença

Desenvolvido por Braz Daniel
