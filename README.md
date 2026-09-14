# API Test Manager

API Mock desenvolvida em Python com FastAPI para simulação de respostas de APIs e apoio em testes de aplicações e fluxos de URA.

## Objetivo

O objetivo deste projeto é disponibilizar uma API local para testes, permitindo simular diferentes cenários sem depender de serviços externos.

A aplicação utiliza massas de dados em JSON e permite testar respostas como:

- Cliente localizado ou não localizado
- Um ou múltiplos contratos
- Diferentes bandeiras de cartão
- Diferentes dias de atraso
- Segunda via de boleto
- Retornos HTTP como 200 e 404
- Cenários com 1, 2, 3 ou mais boletos

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- JSON
- Git
- GitHub
- Swagger / OpenAPI

## Estrutura do projeto

```text
api-test-manager/
├── main.py
├── massa.json
├── requirements.txt
├── README.md
└── .gitignore