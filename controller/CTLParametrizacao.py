from model import DBParametrizacao  as db
from dto import DTOParametrizacao as dt
from entity import Parametrizacao as en
from dataframe import DFParametrizacao as dfPa
from entity import PermissaoDiretorio as entPer
import os

def carregar() -> en.Parametrizacao:
    df = db.DBParametrizacao().consultarTodos()
    dtoParametrizacao = dt.DTOParametrizacao()
    #df = dbParametrizacao.consultarTodos()
    dtoParametrizacao.carregarDF(df)
    obj = en.Parametrizacao()
    obj.carregar(dtoParametrizacao.lista)
    return obj

def salvar(entidade: en.Parametrizacao):
    df = dfPa.DFParametrizacao().criarDF(entidade)
    db.DBParametrizacao().salvar(df)
    
def validarPermissaoEscrita(diretorio: str) -> bool:
    if not os.path.isdir(diretorio):
        return  False
    obj =entPer.PermissaoDiretorio()
    obj.verificarPermissaoDiretorio(diretorio)
    return obj.escrita
        