from pydantic import BaseModel, Field, model_validator

class Contrato(BaseModel):
    contratoOrigem: str
    diasAtrasoContrato: int = Field(ge=0)
    codigoCarteira: str
    numeroDoCartao: str
    
class IdentificacaoCartao(BaseModel):
    clienteLocalizado: bool
    clienteLocalizadoAPICartao: bool
    quantidadeDividas: int = Field(ge=0)
    nomeCliente: str
    contratos: list[Contrato]

    @model_validator(mode="after")
    def validar_quantidade_dividas(self):
        if self.quantidadeDividas != len(self.contratos):
            raise ValueError(
                "quantidadeDividas deve ser igual à quantidade de contratos"
            )

        return self
    
class Boleto(BaseModel):
    linhaDigitavel: str
    descricaoBandeira: str
    contratoOrigem: str    

class ScenarioSummary(BaseModel):
    identificador: str
    carteira: str
    cenario: str
 
class ScenarioCreate(BaseModel):
    identificador: str
    carteira: str
    cenario: str
    identificacao_cartao: IdentificacaoCartao
    segunda_via_cartao: list[Boleto]  