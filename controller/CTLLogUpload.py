import pandas as pd
from model import DBLogUpload as dbLog
from entity import  LogUpload as entLog
from entity import Contratante as entCont

def criarDF(df_logupload: pd.DataFrame)-> pd.DataFrame:
    df_logupload = df_logupload.rename(columns={ "Nome": "UplNome",
                             "Tipo": "UplTipo",
                             "Operador": "UplOperador",
                             "Resultado": "UplResultado",
                             "Processamento": "UplProcessamento",})
    return df_logupload

def criarDFUnico(logUpload: entLog.LogUpload)-> pd.DataFrame:
    df = {'UplNome': [logUpload.Nome], 
            'UplTipo': [logUpload.Tipo], 
            'UplOperador': [logUpload.Operador], 
            'UplResultado': [logUpload.Resultado], 
            'UplProcessamento': [logUpload.Processamento]}
    return pd.DataFrame(df)

def salvar(logUpload: entLog.LogUpload) -> bool:
    df = criarDFUnico(logUpload)
    return dbLog.DBLogUpload().salvar(df)

def consultar() -> pd.DataFrame:
    return dbLog.DBLogUpload().consultar()
    
