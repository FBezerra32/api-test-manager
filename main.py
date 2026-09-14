import json

from fastapi import FastAPI, HTTPException


app = FastAPI(
    title="API Test Manager",
    description="API Mock para testes de aplicações e URAs",
    version="1.0.0"
)


def carregar_massa():
    with open("massa.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


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
    massa = carregar_massa()

    clientes = massa["clientes"]

    if identificador not in clientes:
        raise HTTPException(
            status_code=404,
            detail="Massa não encontrada"
        )

    cliente = clientes[identificador]

    if cliente["carteira"] != carteira:
        raise HTTPException(
            status_code=404,
            detail="Carteira não encontrada"
        )

    return cliente["identificacao_cartao"]


@app.post("/SegundaViaBoleto/Cartao/{identificador}/{carteira}")
def segunda_via_cartao(
    identificador: str,
    carteira: str
):
    massa = carregar_massa()

    clientes = massa["clientes"]

    if identificador not in clientes:
        raise HTTPException(
            status_code=404,
            detail="Massa não encontrada"
        )

    cliente = clientes[identificador]

    if cliente["carteira"] != carteira:
        raise HTTPException(
            status_code=404,
            detail="Carteira não encontrada"
        )

    return cliente["segunda_via_cartao"]