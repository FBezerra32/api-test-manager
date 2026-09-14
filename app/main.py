import json
from pathlib import Path

from fastapi import FastAPI, HTTPException


app = FastAPI(
    title="API Test Manager",
    description="API Mock para testes de aplicações e URAs",
    version="1.0.0"
)


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


@app.get("/")
def inicio():
    return {
        "mensagem": "API Test Manager funcionando!"
    }


@app.post("/ConsultarCliente/Cartao/{identificador}/{carteira}")
def consultar_cliente_cartao(
    identificador: str,
    carteira: str
):
    cliente = localizar_cliente(
        identificador,
        carteira
    )

    return cliente["identificacao_cartao"]


@app.post("/SegundaViaBoleto/Cartao/{identificador}/{carteira}")
def segunda_via_cartao(
    identificador: str,
    carteira: str
):
    cliente = localizar_cliente(
        identificador,
        carteira
    )

    return cliente["segunda_via_cartao"]