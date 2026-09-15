from fastapi import FastAPI

from app.routes.scenarios import router as scenarios_router
from app.routes.mocks import router as mocks_router


app = FastAPI(
    title="API Test Manager",
    description=(
        "API para criação e execução de cenários de teste, "
        "simulação de respostas e apoio a testes de integrações REST."
    ),
    version="1.0.0"
)

app.include_router(scenarios_router)
app.include_router(mocks_router)


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