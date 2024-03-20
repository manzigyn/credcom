from dataclasses import dataclass
import mysql.connector as my
import pandas as pd
from funcoes import utilidades as ut

@dataclass
class Pagamento():
    def importaDF(df, arquivo) -> pd.DataFrame:
        df.dropna(subset=['Dta Pgto Parcela'], inplace=True)
        df["PagDataPagamentoParcela"] = pd.to_datetime(df["Dta Pgto Parcela"])
        df["PagAno"] = df["PagDataPagamentoParcela"].apply((lambda x: str(x.year)))
        df["PagMes"] = df["PagDataPagamentoParcela"].apply((lambda x: int(x.month)))
        df["PagArquivoProcessado"] = ut.formatarArquivoDataModificacao(arquivo)
        df = df.rename(columns={ "Contratante": "PagCpfCnpj",
                                "CPF  CNPJ"    : "PagCpfCnpj",
                                "Nome do Cliente" : "PagNomeCliente",
                                "Parcelas e Data Calculo" : "PagParcelaDataCalculo",
                                "Tipo de Negociação" : "PagTipoNegociacao",
                                "Venda - Quadra - Lote" : "PagVendaQuadraLote",
                                "Data Acordo" : "PagDataAcordo",
                                "Nr. Acordo" : "PagNumeroAcordo",
                                "Vlr. Honorário Acordo" : "PagValorHonorarioAcordo",
                                "Vlr. Total Acordo" : "PagValorTotalAcordo",
                                "Dta Vecto Parcela" : "PagVencimentoParcela",
                                "Dta Pgto Parcela": "PagDataPagamentoParcela",
                                "Bol. Nosso Número": "PagNossoNumero",
                                "Nome Cobrador": "PagNomeCobrador",
                                "Status": "PagStatus",
                                "Empreendimento": "PagEmpreendimento",
                                "Valor parcela": "PagValorParcela",
                                "Recuperado": "PagRecuperado"})
        return df