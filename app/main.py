from fastapi import FastAPI

from app.routes.scenarios import router as scenarios_router
from app.services.scenario_service import localizar_cliente


app = FastAPI(
    title="API Test Manager",
    description=(
        "API para criação e execução de cenários de teste, "
        "simulação de respostas e apoio a testes de integrações REST."
    ),
    version="1.0.0"
)

app.include_router(scenarios_router)


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