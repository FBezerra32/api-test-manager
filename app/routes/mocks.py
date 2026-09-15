from fastapi import APIRouter

from app.services.scenario_service import localizar_cliente


router = APIRouter(
    tags=["Mock API"]
)


@router.post(
    "/ConsultarCliente/Cartao/{identificador}/{carteira}",
    summary="Simula consulta de cliente",
    description="Retorna os dados de identificação configurados para o cenário informado."
)
def consultar_cliente_cartao(identificador: str, carteira: str):
    cliente = localizar_cliente(identificador, carteira)
    return cliente["identificacao_cartao"]


@router.post(
    "/SegundaViaBoleto/Cartao/{identificador}/{carteira}",
    summary="Simula consulta de segunda via",
    description="Retorna os dados de segunda via configurados para o cenário informado."
)
def segunda_via_cartao(identificador: str, carteira: str):
    cliente = localizar_cliente(identificador, carteira)
    return cliente["segunda_via_cartao"]