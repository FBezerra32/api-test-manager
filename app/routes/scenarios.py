from fastapi import APIRouter

from app.services.scenario_service import listar_cenarios


router = APIRouter(
    prefix="/scenarios",
    tags=["Scenarios"]
)


@router.get("")
def obter_cenarios():
    return listar_cenarios()