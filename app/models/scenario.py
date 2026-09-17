from pydantic import BaseModel

class Contrato(BaseModel):
    contratoOrigem: str
    diasAtrasoContrato: int
    codigoCarteira: str
    numeroDoCartao: str
    
class IdentificacaoCartao(BaseModel):
    clienteLocalizado: bool
    clienteLocalizadoAPICartao: bool
    quantidadeDividas: int
    nomeCliente: str
    contratos: list[Contrato]
    
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