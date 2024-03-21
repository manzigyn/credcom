from matplotlib.figure import Figure
import pandas as pd

class ApresentacaoExcel:
    def __init__(self, 
                 Contratante: str,
                 Ano: int,
                 Mes: int,
                 df_loteamento_caixa: pd.DataFrame, 
                 df_loteamento_recuperado: pd.DataFrame, 
                 df_loteamento_tipo: pd.DataFrame,
                 df_loteamento_statusvirtua: pd.DataFrame,
                 df_statusvirtua_quantidade: pd.DataFrame,
                 Sms: int,
                 Ligacao: int, 
                 fig_loteamento_caixa: Figure, 
                 NomeArquivo = '',
                 CaminhoArquivo = ''):
        self.Contratante = Contratante
        self.Ano = Ano
        self.Mes = Mes
        self.df_loteamento_caixa = df_loteamento_caixa
        self.df_loteamento_recuperado = df_loteamento_recuperado
        self.df_loteamento_tipo = df_loteamento_tipo
        self.df_loteamento_statusvirtua = df_loteamento_statusvirtua
        self.df_statusvirtua_quantidade = df_statusvirtua_quantidade
        self.Sms = Sms
        self.Ligacao =Ligacao
        self.fig_loteamento_caixa = fig_loteamento_caixa
        self.NomeArquivo = NomeArquivo
        self.CaminhoArquivo = CaminhoArquivo