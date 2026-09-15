import json
from pathlib import Path

from fastapi import FastAPI, HTTPException

from app.routes.scenarios import router as scenarios_router



app = FastAPI(
    title="API Test Manager",
    description=(
        "API para criação e execução de cenários de teste, "
        "simulação de respostas e apoio a testes de integrações REST."
    ),
    version="1.0.0"
)

app.include_router(scenarios_router)

BASE_DIR = Path(__file__).resolve().parent
CAMINHO_MASSA = BASE_DIR / "data" / "massa.json"


def carregar_massa():
    with open(CAMINHO_MASSA, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def localizar_cliente(identificador: str, carteira: str):
    massa = carregar_massa()

    clientes = massa.get("clientes", {})

    if identificador not in clientes:
        raise HTTPException(
            status_code=404,
            detail="Massa não encontrada"
        )

    cliente = clientes[identificador]

    if cliente.get("carteira") != carteira:
        raise HTTPException(
            status_code=404,
            detail="Carteira não encontrada"
        )

    return cliente


@app.get(
    "/",
    tags=["Status"],
    summary="Verifica o status da API",
    description="Endpoint simples para validar se a API está em execução."
)
def inicio():
    return {
        "status": "ok",
        "mensagem": "API Test Manager funcionando!"
    }


@app.post(
    "/ConsultarCliente/Cartao/{identificador}/{carteira}",
    tags=["Mock API"],
    summary="Simula consulta de cliente",
    description="Retorna os dados de identificação configurados para o cenário informado."
)
def consultar_cliente_cartao(identificador: str, carteira: str):
    cliente = localizar_cliente(identificador, carteira)
    return cliente["identificacao_cartao"]


@app.post(
    "/SegundaViaBoleto/Cartao/{identificador}/{carteira}",
    tags=["Mock API"],
    summary="Simula consulta de segunda via",
    description="Retorna os dados de segunda via configurados para o cenário informado."
)
def segunda_via_cartao(identificador: str, carteira: str):
    cliente = localizar_cliente(identificador, carteira)
    return cliente["segunda_via_cartao"]