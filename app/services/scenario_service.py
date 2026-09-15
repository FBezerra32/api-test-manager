import json
from pathlib import Path

from fastapi import HTTPException


BASE_DIR = Path(__file__).resolve().parent.parent
CAMINHO_MASSA = BASE_DIR / "data" / "massa.json"


def carregar_massa():
    with open(CAMINHO_MASSA, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def listar_cenarios():
    massa = carregar_massa()

    clientes = massa.get("clientes", {})
    cenarios = []

    for identificador, cliente in clientes.items():
        cenarios.append({
            "identificador": identificador,
            "carteira": cliente.get("carteira"),
            "cenario": cliente.get("cenario")
        })

    return cenarios


def buscar_cenario(identificador: str):
    massa = carregar_massa()

    clientes = massa.get("clientes", {})

    return clientes.get(identificador)


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