import pandas as pd
from entity import ConfiguracaoResultado as entConf
from view import ViewLoteamentoCaixa as vwLotCaixa

class ApresentacaoExcel:
    def __init__(self, 
                 configuracaoResultado: entConf.ConfiguracaoResultado,
                 viewLoteamentoCaixa: vwLotCaixa.ViewLoteamentoCaixa, 
                 df_loteamento_recuperado: pd.DataFrame, 
                 df_loteamento_tipo: pd.DataFrame,
                 df_loteamento_statusvirtua: pd.DataFrame,
                 df_statusvirtua_quantidade: pd.DataFrame,
                 NomeArquivo = '',
                 CaminhoArquivo = ''):
        self.Contratante = configuracaoResultado.contratante.nome
        self.Ano = configuracaoResultado.contratante.ano
        self.Mes = configuracaoResultado.contratante.mes
        self.df_loteamento_caixa = viewLoteamentoCaixa.apresentacaoView.df_tabela
        self.df_loteamento_recuperado = df_loteamento_recuperado
        self.df_loteamento_tipo = df_loteamento_tipo
        self.df_loteamento_statusvirtua = df_loteamento_statusvirtua
        self.df_statusvirtua_quantidade = df_statusvirtua_quantidade
        self.Sms = configuracaoResultado.sms
        self.Ligacao =configuracaoResultado.ligacao
        self.fig_loteamento_caixa = viewLoteamentoCaixa.apresentacaoView.grafico
        self.NomeArquivo = NomeArquivo
        self.CaminhoArquivo = CaminhoArquivo