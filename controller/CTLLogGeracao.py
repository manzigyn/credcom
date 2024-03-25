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

def consultarAnoMesDistinto() -> pd.DataFrame:
    return dbLog.DBLogGeracao().consultarAnoMesDistinto()
    
def obterListaAno(df: pd.DataFrame) -> list:
    return df["Ano"].unique()
    
def obterListaMes(df: pd.DataFrame) -> list:
    return df["Mes"].unique()

def consultar(contratante: entCont.Contratante, padrao: str, somenteNaoGerados: bool)-> pd.DataFrame:
    df = dbLog.DBLogGeracao().consultar()
    if contratante.nome != padrao:
        df = df[df['Contratante'] == contratante.nome]
    if contratante.ano != padrao:
        df = df[df['Ano'] == int(contratante.ano)]
    if contratante.mes != padrao:
        df = df[df['Mes'] == int(contratante.mes)]
    if somenteNaoGerados:
        df = df[pd.isna(df['Data'])]

    return df