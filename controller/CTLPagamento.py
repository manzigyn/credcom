import pandas as pd
from utils import utilidades as ut
from utils import pandas_files as pf
from model import DBPagamento as dbPgto
from entity import Contratante as entCont

def importarDF(df, arquivo) -> pd.DataFrame:
    df.dropna(subset=['Contratante'], inplace=True)
    #Conversão de datas
    df["PagVencimentoParcela"] = pd.to_datetime(df["Dta Vecto Parcela"])
    df["PagDataAcordo"] = pd.to_datetime(df["Data Acordo"])
    df["PagDataPagamentoParcela"] = pd.to_datetime(df["Dta Pgto Parcela"])
    df["PagAno"] = df["PagDataPagamentoParcela"].apply((lambda x: str(x.year)))
    df["PagMes"] = df["PagDataPagamentoParcela"].apply((lambda x: int(x.month)))
    #Conversão de valores monetários
    df['PagValorHonorarioAcordo'] = df['Vlr. Honorário Acordo'].apply((lambda x: ut.tratarMoedaReal(x)))
    df['PagValorHonorarioAcordo'] = df['PagValorHonorarioAcordo'].astype(float)
    
    df['PagValorTotalAcordo'] = df['Vlr. Total Acordo'].apply((lambda x: ut.tratarMoedaReal(x)))
    df['PagValorTotalAcordo'] = df['PagValorTotalAcordo'].astype(float)
    
    df['PagValorParcela'] = df['Valor parcela'].apply((lambda x: ut.tratarMoedaReal(x)))
    df['PagValorParcela'] = df['PagValorParcela'].astype(float)
    
    df['PagValorRecuperado'] = df['Recuperado'].apply((lambda x: ut.tratarMoedaReal(x)))
    df['PagValorRecuperado'] = df['PagValorRecuperado'].astype(float)
    
    df["PagArquivoProcessado"] = ut.formatarArquivoDataModificacao(arquivo)
    
    df = df.rename(columns={ "Contratante": "PagContratante",
                            "CPF  CNPJ"    : "PagCpfCnpj",
                            "Nome do Cliente" : "PagNomeCliente",
                            "Parcelas e Data Calculo" : "PagParcelaDataCalculo",
                            "Tipo de Negociação" : "PagTipoNegociacao",
                            "Venda - Quadra - Lote" : "PagVendaQuadraLote",
                            "Nr. Acordo" : "PagNumeroAcordo",
                            "Bol. Nosso Número": "PagNossoNumero",
                            "Nome Cobrador": "PagNomeCobrador",
                            "Status": "PagStatus",
                            "Empreendimento": "PagEmpreendimento"})
    
    df["PagEmpreendimento"] = df["PagEmpreendimento"].str.title()
    
    df = df[["PagAno",
            "PagMes",
            "PagContratante",
            "PagCpfCnpj",
            "PagNomeCliente",
            "PagParcelaDataCalculo",
            "PagTipoNegociacao",
            "PagVendaQuadraLote",
            "PagDataAcordo",
            "PagNumeroAcordo",
            "PagValorHonorarioAcordo",
            "PagValorTotalAcordo",
            "PagVencimentoParcela",
            "PagDataPagamentoParcela",
            "PagNossoNumero",
            "PagNomeCobrador",
            "PagStatus",
            "PagEmpreendimento",
            "PagValorParcela",
            "PagValorRecuperado",
            "PagArquivoProcessado"]]
    return df

def apresentarDFOriginal(df) -> pd.DataFrame:
    df = df.rename(columns={ "PagContratante": "Contratante" ,
                            "PagCpfCnpj" :"CPF  CNPJ" ,
                            "PagNomeCliente" : "Nome do Cliente",
                            "PagParcelaDataCalculo": "Parcelas e Data Calculo",
                            "PagTipoNegociacao" : "Tipo de Negociação",
                            "PagVendaQuadraLote" : "Venda - Quadra - Lote",
                            "PagDataAcordo" : "Data Acordo",
                            "PagNumeroAcordo": "Nr. Acordo" ,
                            "PagValorHonorarioAcordo":"Vlr. Honorário Acordo",                                
                            "PagValorTotalAcordo": "Vlr. Total Acordo",
                            "PagVencimentoParcela" : "Dta Vecto Parcela",
                            "PagDataPagamentoParcela" : "Dta Pgto Parcela",
                            "PagNossoNumero" : "Bol. Nosso Número",
                            "PagNomeCobrador" : "Nome Cobrador",
                            "PagStatus" : "Status",
                            "PagEmpreendimento" : "Empreendimento",
                            "PagValorParcela" : "Valor parcela",
                            "PagValorRecuperado" : "Recuperado",
                            "PagAno": "Ano",
                            "PagMes": "Mês",
                            "PagArquivoProcessado": "Arquivo Processado"})
    return df

def salvar(arquivo) -> bool:
    df = pf.lerExcelTipado(arquivo,{'Vlr. Honorário Acordo': str, 'Vlr. Total Acordo': str, 'Valor parcela': str, 'Recuperado': str})                         
    df_pagamento = importarDF(df,arquivo)
    
    dbPagamento = dbPgto.DBPagamento()        
    return dbPagamento.salvar(df_pagamento)

def consultarContratantesDistintos() -> pd.DataFrame:
    return dbPgto.DBPagamento().consultarContratanteDistinto()
    
def consultarContratante(nome: str) -> pd.DataFrame:
    return dbPgto.DBPagamento().consultarContratante(nome)
    
def obterListaContratante(df: pd.DataFrame) -> list:
    return df["Contratante"].unique()

def obterListaAno(df: pd.DataFrame) -> list:
    return df["PagAno"].unique()
    
def obterListaMes(df: pd.DataFrame) -> list:
    return df["PagMes"].unique()

def consultarLoteamentoValorPago(contratante: entCont.Contratante) -> pd.DataFrame:
    return dbPgto.DBPagamento().consultarLoteamentoValorPago(contratante)

def consultarLoteamentoValorRecuperado(contratante: entCont.Contratante) -> pd.DataFrame:
    return dbPgto.DBPagamento().consultarLoteamentoValorRecuperado(contratante)

def consultarTipoNegociacao(contratante: entCont.Contratante) -> pd.DataFrame:
    return dbPgto.DBPagamento().consultarTipoNegociacao(contratante)