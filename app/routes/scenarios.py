from fastapi import APIRouter, HTTPException

from app.services.scenario_service import listar_cenarios, buscar_cenario


router = APIRouter(
    prefix="/scenarios",
    tags=["Scenarios"]
)

@router.get("")
def obter_cenarios():
    return listar_cenarios()

@router.get("/{identificador}")
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