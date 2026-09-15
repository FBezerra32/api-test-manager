from pydantic import BaseModel


class ScenarioSummary(BaseModel):
    identificador: str
    carteira: str
    cenario: str
    
class ScenarioCreate(BaseModel):
    identificador: str
    carteira: str
    cenario: str    