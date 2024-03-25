import locale
import streamlit as st
from controller import CTLApresentacaoResultado
from controller import CTLPagamento 
from controller import CTLDistribuicao
from controller import CTLParametrizacao
from entity import ApresentacaoExcel as entAp
from entity import Contratante as entCont
from entity import ConfiguracaoResultado as entConfig
from entity import ApresentacaoResultado as entApre
from view import ViewLoteamentoCaixa as vwLotCaixa
from view import ViewLoteamentoRecuperado as vwLotRecup
from view import ViewLoteamentoTipo as vwLotTipo
from view import ViewLoteamentoStatusVirtua as vwLotVirtua
from view import ViewStatusVirtuaQuantidade as vwSta
from view import ViewImportarArquivoExcel as vwArqExcel
from view import ViewGerarApresentacao as vwGerApre
from view import ViewParametrizacao as vwConfig
from utils import utilidades as ut

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
#pd.options.display.float_format = 'R${:, .2f}'.format

st.set_page_config(
    page_title="Gestão de Resultados da Credcom",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)
#st.sidebar.image('img/logo.png')
ut.adicionar_logo('img/logo.png')


entContratante = entCont.Contratante()
entConfiguracaoResultado = entConfig.ConfiguracaoResultado()
entApresentacaoResultado = entApre.ApresentacaoResultado()
viewLoteamentoCaixa = vwLotCaixa.ViewLoteamentoCaixa()
viewLoteamentoRecuperado = vwLotRecup.ViewLoteamentoRecuperado()
viewLoteamentoTipo = vwLotTipo.ViewLoteamentoTipo()
viewLoteamentoStatusVirtua = vwLotVirtua.ViewLoteamentoStatusVirtua()
viewStatusVirtuaQuantidade = vwSta.ViewStatusVirtuaQuantidade()
viewGerarApresentacao = vwGerApre.ViewGerarApresentacao()
viewConfiguracao = vwConfig.ViewParametrizacao()

ctlParametrizacao = CTLParametrizacao.carregar()

df_contratante = CTLPagamento.consultarContratantesDistintos()

if ctlParametrizacao.haCarga():
    vwArqExcel.ViewImportarArquivoExcel().criar()

entContratante.nome = st.sidebar.selectbox("Contratante", options=['Selecione...']+list(CTLPagamento.obterListaContratante(df_contratante)))
 

label = f'Apresentação de Resultados - {entContratante.nome}'
s = f"<p style='font-size:30px; font-weight: bold'>{label}</p>"
st.markdown(s, unsafe_allow_html=True)


tab_apresentacao, tab_configuracao, tab_dados  = st.tabs([":moneybag: Apresentação",":mailbox_with_mail: Configuração", ":books: Dados"])
if entContratante.nome != 'Selecione...':    
    entApresentacaoResultado = CTLApresentacaoResultado.obter(entContratante)
    entContratante.ano = st.sidebar.selectbox("Ano", entApresentacaoResultado.anos)
    entContratante.mes = st.sidebar.selectbox("Mês", entApresentacaoResultado.meses)

    with st.container():
        with tab_apresentacao:
            r_ap1 = st.columns(2)
            r_ap2 = st.columns(2)
            r_ap3 = st.columns(2)
            #r_ap4 = st.columns(1)
            r_ap5 = st.columns(2)
            altura = 380
            
            #Loteamento por Caixa            
            viewLoteamentoCaixa.criar(entContratante, r_ap1, altura)

            #Loteamento por valor recuperado
            viewLoteamentoRecuperado.criar(entContratante)
            
            viewLoteamentoStatusVirtua.inicializar(entContratante)            
            if not viewLoteamentoStatusVirtua.haStatus():
                viewLoteamentoRecuperado.atualizaDados(r_ap2, altura)
           
            #Loteamento por tipo de negociação
            viewLoteamentoTipo.criar(entContratante, r_ap3, altura)
            
            
            #Loteamento por status virtua
            if viewLoteamentoStatusVirtua.haStatus():                        
                #Loteamento por valor recuperado
                viewLoteamentoRecuperado.atualizaDados(r_ap2, altura)
                
                viewLoteamentoStatusVirtua.criar(r_ap3,altura, viewLoteamentoRecuperado.apresentacaoView.df_tabela)
            else:
                r_ap3[1].warning(f"Não há configuração dos status virtua definido para Contratante {entContratante.nome} em {entContratante.mes}/{entContratante.ano}")              
           
            #Status Virtua Quantidade
            viewStatusVirtuaQuantidade.criar(entContratante, r_ap5, altura)
        

        with tab_configuracao:
           viewConfiguracao.criar(entContratante)
                                    
     

        with tab_dados:
            r_da1 = st.columns(1)
            r_da2 = st.columns(1)
            
            r_da1[0].write("Dados de Pagamento")
            r_da1[0].dataframe(CTLPagamento.apresentarDFOriginal(entApresentacaoResultado.df_pagamento))
            r_da2[0].write("Dados de Distribuição")
            r_da2[0].dataframe(CTLDistribuicao.apresentarDFOriginal(entApresentacaoResultado.df_distribuicao))
            
   
   
    apresentacaoExcel = entAp.ApresentacaoExcel(viewConfiguracao.configuracaoResultado,
                                                viewLoteamentoCaixa, 
                                                viewLoteamentoRecuperado,
                                                viewLoteamentoTipo,
                                                viewLoteamentoStatusVirtua,
                                                viewStatusVirtuaQuantidade
                                                )
    viewGerarApresentacao.criar(apresentacaoExcel, not viewLoteamentoStatusVirtua.haStatus())
    
        

       