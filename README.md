# 🚀 API Test Manager

API Mock desenvolvida em **Python** com **FastAPI** para criação e execução de cenários de teste, simulação de respostas de APIs e apoio em testes de aplicações e fluxos de URA.

O projeto permite criar massas de teste locais e simular diferentes comportamentos de uma API sem depender de serviços externos.

---

## 🎯 Objetivo

O objetivo do **API Test Manager** é facilitar testes de integração através de uma API Mock simples, organizada e extensível.

A aplicação permite trabalhar com diferentes cenários, como:

- Cliente localizado ou não localizado
- Um ou múltiplos contratos
- Diferentes bandeiras de cartão
- Diferentes dias de atraso
- Segunda via de boleto
- Cenários com 1, 2, 3 ou mais boletos
- Retornos HTTP como `200`, `201`, `404`, `409` e `422`
- Validação de dados de entrada
- Persistência de cenários em JSON

---

## 🛠️ Tecnologias utilizadas

- Python 3.11
- FastAPI
- Pydantic
- Uvicorn
- JSON
- Swagger / OpenAPI
- Git
- GitHub

---

## 📁 Estrutura do projeto

```text
api-test-manager/
│
├── app/
│   ├── data/
│   │   └── massa.json
│   │
│   ├── models/
│   │   └── scenario.py
│   │
│   ├── routes/
│   │   ├── mocks.py
│   │   └── scenarios.py
│   │
│   ├── services/
│   │   └── scenario_service.py
│   │
│   └── main.py
│
├── docs/
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

A aplicação está organizada em camadas:

- **routes** → definição dos endpoints
- **services** → regras e acesso às massas de teste
- **models** → modelos e validações Pydantic
- **data** → armazenamento das massas JSON

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/FBezerra32/api-test-manager.git
```

Entre na pasta:

```bash
cd api-test-manager
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando a API

Na raiz do projeto, execute:

```bash
python -m uvicorn app.main:app --reload
```

A API ficará disponível em:

```text
http://127.0.0.1:8000
```

---

## 📚 Swagger

A documentação interativa é gerada automaticamente pelo FastAPI.

Acesse:

```text
http://127.0.0.1:8000/docs
```

Através do Swagger é possível executar os endpoints e visualizar os contratos de entrada e saída da API.

---

## 🔗 Endpoints

### Cenários

| Método | Endpoint | Descrição |
|---|---|---|
| `GET` | `/scenarios` | Lista os cenários disponíveis |
| `GET` | `/scenarios/{identificador}` | Consulta um cenário pelo identificador |
| `POST` | `/scenarios` | Cria e persiste um novo cenário |

### Mock API

| Método | Endpoint | Descrição |
|---|---|---|
| `POST` | `/ConsultarCliente/Cartao/{identificador}/{carteira}` | Simula uma consulta de cliente |
| `POST` | `/SegundaViaBoleto/Cartao/{identificador}/{carteira}` | Simula uma consulta de segunda via |

### Status

| Método | Endpoint | Descrição |
|---|---|---|
| `GET` | `/` | Verifica se a API está em execução |

---

## ➕ Criando um cenário

Exemplo de requisição:

```json
{
  "identificador": "666666666000006",
  "carteira": "519",
  "cenario": "teste_criacao"
}
```

Requisição:

```text
POST /scenarios
```

Quando criado com sucesso, a API retorna:

```text
201 Created
```

O cenário é persistido no arquivo de massas da aplicação.

Caso o identificador já exista:

```text
409 Conflict
```

Isso evita que um cenário existente seja sobrescrito acidentalmente.

---

## ✅ Validação com Pydantic

Os dados recebidos pela API são validados através de modelos Pydantic.

Por exemplo, atualmente um cenário possui os campos obrigatórios:

```text
identificador
carteira
cenario
```

Caso um campo obrigatório não seja enviado, a API rejeita a requisição com:

```text
422 Unprocessable Entity
```

---

## 🧪 Cenários de teste

A massa JSON pode representar diferentes comportamentos utilizados nos testes da Mock API.

Atualmente o projeto possui cenários para testar diferentes quantidades de contratos e boletos.

Todos os dados utilizados neste projeto são **fictícios e destinados exclusivamente a testes**.

---

## 🗺️ Roadmap

Próximas evoluções planejadas:

- [x] Estrutura inicial da API
- [x] Massa de testes em JSON
- [x] Consulta de cenários
- [x] Organização em routes e services
- [x] Documentação Swagger
- [x] Modelos Pydantic
- [x] Criação de cenários pela API
- [x] Validação de identificadores duplicados
- [ ] Modelagem completa de contratos
- [ ] Modelagem de boletos
- [ ] Criação de cenários completos pela API
- [ ] Atualização de cenários
- [ ] Exclusão de cenários
- [ ] Testes automatizados
- [ ] Tratamento centralizado de erros
- [ ] Evolução da persistência de dados

---

## 👨‍💻 Autor

**Fabio Bezerra**

Projeto desenvolvido para estudo e prática de:

`Python` • `FastAPI` • `APIs REST` • `Pydantic` • `Git` • `GitHub`