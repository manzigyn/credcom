from entity import ConfiguracaoResultado as entConf
from view import ViewLoteamentoCaixa as vwLotCaixa
from view import ViewLoteamentoRecuperado as vwLotRecup
from view import ViewLoteamentoTipo as vwLotTipo
from view import ViewLoteamentoStatusVirtua as vwLotVirtua
from view import ViewStatusVirtuaQuantidade as vwSta


class ApresentacaoExcel:
    def __init__(self, 
                 configuracaoResultado: entConf.ConfiguracaoResultado,
                 viewLoteamentoCaixa: vwLotCaixa.ViewLoteamentoCaixa, 
                 viewLoteamentoRecuperado: vwLotRecup.ViewLoteamentoRecuperado, 
                 viewLoteamentoTipo: vwLotTipo.ViewLoteamentoTipo, 
                 vViewLoteamentoStatusVirtua: vwLotVirtua.ViewLoteamentoStatusVirtua, 
                 viewStatusVirtuaQuantidade: vwSta.ViewStatusVirtuaQuantidade, 
                 NomeArquivo = '',
                 CaminhoArquivo = ''):
        self.contratante = configuracaoResultado.contratante
        self.df_loteamento_caixa = viewLoteamentoCaixa.apresentacaoView.df_tabela
        self.df_loteamento_recuperado = viewLoteamentoRecuperado.apresentacaoView.df_tabela
        self.df_loteamento_tipo = viewLoteamentoTipo.apresentacaoView.df_tabela
        self.df_loteamento_statusvirtua = vViewLoteamentoStatusVirtua.apresentacaoView.df_tabela
        self.df_statusvirtua_quantidade = viewStatusVirtuaQuantidade.apresentacaoView.df_tabela
        self.sms = configuracaoResultado.sms
        self.ligacao =configuracaoResultado.ligacao
        self.fig_loteamento_caixa = viewLoteamentoCaixa.apresentacaoView.grafico
        self.nomeArquivo = NomeArquivo
        self.caminhoArquivo = CaminhoArquivo
        self.gr_loteamento_caixa = viewLoteamentoCaixa.apresentacaoView.grafico