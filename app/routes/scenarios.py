from fastapi import APIRouter, HTTPException

from app.services.scenario_service import listar_cenarios, buscar_cenario


router = APIRouter(
    prefix="/scenarios",
    tags=["Scenarios"]
)


@router.get(
    "",
    summary="Lista todos os cenários",
    description="Retorna todos os cenários de teste disponíveis na massa de dados.",
    responses={
        200: {
            "description": "Lista de cenários retornada com sucesso."
        }
    }
)
def obter_cenarios():
    return listar_cenarios()


@router.get(
    "/{identificador}",
    summary="Busca um cenário por identificador",
    description="Retorna os detalhes completos de um cenário específico.",
    responses={
        200: {
            "description": "Cenário encontrado com sucesso."
        },
        404: {
            "description": "Cenário não encontrado."
        }
    }
)
def obter_cenario(identificador: str):
    cenario = buscar_cenario(identificador)

    if cenario is None:
        raise HTTPException(
            status_code=404,
            detail="Cenario nao encontrado"
        )

    return {
        "identificador": identificador,
        **cenario
    }