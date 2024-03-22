import pandas as pd
from utils import utilidades as ut
from utils import pandas_files as pf
from model import DBDistribuicao as dbDis
from entity import Contratante as entCont

def importaDF(df, arquivo) -> pd.DataFrame:
    df["DisArquivoProcessado"] = ut.formatarArquivoDataModificacao(arquivo)
    #Conversão de valores monetários
    df['DisValorTotal'] = df['Valor total'].replace("R$","").replace(".","").replace(",",".").replace(" ","").astype(float)
    df = df.rename(columns={    "Carteira": "DisCarteira",
                                "Operador": "DisOperador",
                                "Nº Parcelas": "DisNumeroParcelas",
                                "Venda": "DisVenda",
                                "Unidade": "DisUnidade",
                                "Cod. Cliente/Contrato": "DisCodigoClienteContrato",
                                "Loteamento/Curso/LUC": "DisLoteamentoCursoLuc",
                                "Atraso real": "DisAtrasoReal",
                                "Status": "DisStatus",
                                "CPF/CNPJ": "DisCpfCnpj",
                                "Nome": "DisNome",
                                "Status 2": "DisStatus2",
                                "Status Virtua": "DisStatusVirtua",})
    
    df["DisLoteamentoCursoLuc"] = df["DisLoteamentoCursoLuc"].str.title()
    
    if "DisUnidade" not in df:
        df["DisUnidade"] = pd.NA
    if "DisVenda" not in df:
        df["DisVenda"] = pd.NA            
    if "DisStatus2" not in df:
        df["DisStatus2"] = pd.NA            
    df = df[["DisCarteira",
                "DisOperador",
                "DisNumeroParcelas",
                "DisVenda",
                "DisUnidade",
                "DisCodigoClienteContrato",
                "DisLoteamentoCursoLuc",
                "DisAtrasoReal",
                "DisValorTotal",
                "DisStatus",
                "DisCpfCnpj",
                "DisNome",
                "DisStatus2",
                "DisStatusVirtua",
                "DisArquivoProcessado"]]
    return df

def apresentarDFOriginal(df) -> pd.DataFrame:  
    df = df.rename(columns={ "DisCarteira" : "Carteira" ,
                                "DisOperador" : "Operador",
                                "DisNumeroParcelas" : "Nº Parcelas",
                                "DisVenda" : "Venda",
                                "DisUnidade" : "Unidade",
                                "DisCodigoClienteContrato" : "Cod. Cliente/Contrato",
                                "DisLoteamentoCursoLuc" : "Loteamento/Curso/LUC" ,
                                "DisAtrasoReal" : "Atraso real" ,
                                "DisValorTotal" :"Valor total",
                                "DisStatus" : "Status",
                                "DisCpfCnpj" : "CPF/CNPJ",
                                "DisNome" : "Nome" ,
                                "DisStatus2" : "Status 2" ,
                                "DisStatusVirtua" : "Status Virtua",
                                "DisAno": "Ano",
                                "DisMes": "Mês",
                                "DisArquivoProcessado": "Arquivo Processado"})  
    return df

def salvar(arquivo) -> bool:
    df = pf.lerExcel(arquivo)    
    df_Distribuicao = importaDF(df, arquivo)
    
    return dbDis.DBDistribuicao().salvar(df_Distribuicao)

    
def consultarContratante(nome: str) -> pd.DataFrame:
    return dbDis.DBDistribuicao().consultarContratante(nome)
    
def consultarLoteamentoValorTotal(contratante: entCont.Contratante) -> pd.DataFrame:
    return dbDis.DBDistribuicao().consultarLoteamentoValorTotal(contratante)

def consultarStatusVirtuaTotal(contratante: entCont.Contratante) -> pd.DataFrame:
    return dbDis.DBDistribuicao().consultarStatusVirtuaTotal(contratante.nome)