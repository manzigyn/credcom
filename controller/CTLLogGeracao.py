import pandas as pd
from model import DBLogGeracao as dbLog
from entity import LogGeracao as entLog
from entity import Contratante as entCont


def criarDFUnico(logGeracao: entLog.LogGeracao)-> pd.DataFrame:
    df = {'GerContratante': [logGeracao.contratante.nome], 
            'GerAno': [int(logGeracao.contratante.ano)], 
            'GerMes': [int(logGeracao.contratante.mes)], 
            'GerOperador': [logGeracao.operador], 
            'GerData': [logGeracao.data],
            'GerHorario': [logGeracao.horario],
            'GerArquivo': [logGeracao.arquivo],
            'GerCaminho': [logGeracao.caminho]}
    return pd.DataFrame(df)

def salvar(contratante: entCont.Contratante, arquivo: str, caminho: str) -> bool:
    logGeracao = entLog.LogGeracao()
    logGeracao.contratante = contratante
    logGeracao.arquivo = arquivo
    logGeracao.caminho = caminho
    df = criarDFUnico(logGeracao)
    return dbLog.DBLogGeracao().salvar(df)

def consultarContratantesDistintos() -> pd.DataFrame:
    return dbLog.DBLogGeracao().consultarAnoMesDistinto()
    
def obterListaAno(df: pd.DataFrame) -> list:
    return df["Ano"].unique()
    
def obterListaMes(df: pd.DataFrame) -> list:
    return df["Mes"].unique()