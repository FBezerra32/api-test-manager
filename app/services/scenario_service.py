import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
CAMINHO_MASSA = BASE_DIR / "data" / "massa.json"


def listar_cenarios():
    with open(CAMINHO_MASSA, "r", encoding="utf-8") as arquivo:
        massa = json.load(arquivo)

    clientes = massa.get("clientes", {})
    cenarios = []

    for identificador, cliente in clientes.items():
        cenarios.append({
            "identificador": identificador,
            "carteira": cliente.get("carteira"),
            "cenario": cliente.get("cenario")
        })

    return cenarios