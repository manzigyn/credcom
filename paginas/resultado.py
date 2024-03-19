import locale
import streamlit as st
from classes import DBConfiguracaoResultado as dbConf
from classes import DBDistribuicao as dbDis
from classes import DBPagamento as dbPag
from classes import Entidades as ent
import pandas as pd
from funcoes import utilidades as ut
import traceback
import plotly_express as px    

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
#pd.options.display.float_format = 'R${:, .2f}'.format

st.set_page_config(
    page_title="Gestão de Resultados da Credcom",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)


dbPagamento = dbPag.DBPagamento()
dbDistribuicao = dbDis.DBDistribuicao()
dbConfiguracao = dbConf.DBConfiguracaoResultado()
#entApresentacao = ent.Apresentacao()
objDadosArquivoExcel = ent.DadosArquivoExcel()

df_contratante = dbPagamento.consultarContratanteDistinto()
gAno = -1
gMes = -1
gSms = 0
gLigacao = 0


st.sidebar.image('img/logo.png')
if objDadosArquivoExcel.haNovosArquivos():
    st.warning(f'Pagamento {len(objDadosArquivoExcel.lista_pagamento)} Distribuição: {len(objDadosArquivoExcel.lista_distribuicao)}')
    if st.button('Atualizar Arquivos',type='primary'):
        try:
            objDadosArquivoExcel.processarArquivos()
            st.success("Arquivos atualizados com sucesso")
        except Exception as e:
            mensagem = traceback.format_exc()
            with st.expander('Falha no processamento do arquivo'):
                st.markdown(mensagem)
    
gContratante = st.sidebar.selectbox("Contratante", options=['Selecione...']+list(df_contratante["Contratante"].unique()))

label = f'Apresentação de Resultados - {gContratante}'
s = f"<p style='font-size:30px; font-weight: bold'>{label}</p>"
st.markdown(s, unsafe_allow_html=True)


tab_apresentacao, tab_configuracao, tab_dados  = st.tabs([":moneybag: Apresentação",":mailbox_with_mail: Configuração", ":books: Dados"])
if gContratante != 'Selecione...':    
    df_dados_pagamento = dbPagamento.consultarContratante(gContratante)
    df_dados_distribuicao = dbDistribuicao.consultarContratante(gContratante)
    
    df_filtro = df_dados_pagamento[df_dados_pagamento['PagContratante'] == gContratante]
    gAno = st.sidebar.selectbox("Ano", df_dados_pagamento['PagAno'].unique())
    gMes = st.sidebar.selectbox("Mês", df_dados_pagamento['PagMes'].unique())

    with st.container():
        with tab_apresentacao:
            r_ap1 = st.columns(2)
            r_ap2 = st.columns(2)
            r_ap3 = st.columns(1)
            r_ap4 = st.columns(1)
            r_ap5 = st.columns(2)
            altura = 380
            
            #Loteamento por Caixa
            df_loteamento_caixa = dbPagamento.consultarLoteamentoValorPago(gContratante, gAno, gMes)
            #colwidth = df_loteamento_caixa["Loteamento"].str.len().max()
            #pd.set_option('max_colwidth', int(colwidth))
            df_loteamento_caixa["Valor em Caixa"] = df_loteamento_caixa["Total"].apply(lambda x: ut.formatarMoedaReal(x))            
            row_df ={"Loteamento" :"Total geral", "Valor em Caixa" : ut.formatarMoedaReal(df_loteamento_caixa["Total"].sum())}            
                        
            fig_loteamento_caixa = px.pie(df_loteamento_caixa, values='Total', names='Loteamento',
                                          labels={"Total":"Valor em Caixa"},
                                        title='Loteamento por Valor em Caixa', opacity=0.80)
            fig_loteamento_caixa.update_traces(textinfo='percent')
            
            
            #df_loteamento_caixa = df_loteamento_caixa.drop("Total", axis=1)
            
            #Grafico
            r_ap1[1].container(height=altura+80).plotly_chart(fig_loteamento_caixa, use_container_with=True)
            
            #Tabela
            df_loteamento_caixa.loc[len(df_loteamento_caixa)] = row_df
            r_ap1[0].container(height=altura+80).dataframe(df_loteamento_caixa[["Loteamento","Valor em Caixa"]], hide_index=True, width=altura+80)            
            #r_ap1[0].info(f'Total geral: {ut.formatarMoedaReal(df_loteamento_caixa_total)}')


            #Loteamento por valor recuperado
            df_loteamento_recuperado = dbPagamento.consultarLoteamentoValorRecuperado(gContratante, gAno, gMes)
            df_loteamento_recuperado["Valor Recuperado"] = df_loteamento_recuperado["Total"].apply(lambda x: ut.formatarMoedaReal(x))            
            row_df_recuperado ={"Loteamento" :"Total geral", "Valor Recuperado" : ut.formatarMoedaReal(df_loteamento_recuperado["Total"].sum())}            
            
            fig_loteamento_recuperado = px.pie(df_loteamento_recuperado, values='Total', names='Loteamento',
                                          labels={"Total":"Valor Recuperado"},
                                        title='Loteamento por Valor Recuperado', opacity=0.80)
            fig_loteamento_recuperado.update_traces(textinfo='percent')
            
            df_loteamento_statusvirtua_aux = dbDistribuicao.consultarLoteamentoValorTotal(gContratante, gAno, gMes)
            if df_loteamento_statusvirtua_aux.empty:
                #df_loteamento_recuperado = df_loteamento_recuperado.drop("Total", axis=1)            
                #Grafico Loteamento por valor recuperado
                r_ap2[1].container(height=altura+80).plotly_chart(fig_loteamento_recuperado, use_container_with=True)                
                #Tabela Loteamento por valor recuperado
                df_loteamento_recuperado.loc[len(df_loteamento_recuperado)] = row_df
                r_ap2[0].container(height=altura+80).dataframe(df_loteamento_recuperado[["Loteamento","Valor Recuperado"]], hide_index=True, width=altura+80)
            
            #r_ap2[0].info(f'Total geral: {ut.formatarMoedaReal(df_loteamento_recuperado_total)}')
            
            #Loteamento por tipo de negociação
            df_loteamento_tipo = dbPagamento.consultarTipoNegociacao(gContratante, gAno, gMes)
            df_loteamento_tipo["Valor Recuperado"] = df_loteamento_tipo["Total"].apply(lambda x: ut.formatarMoedaReal(x))
            #df_loteamento_tipo_total = df_loteamento_tipo["Total"].sum()
            #df_loteamento_tipo_quantidade_total = df_loteamento_tipo["Qtde"].sum()
            
            row_df ={"Tipo" :"Total geral","Qtde" : df_loteamento_tipo["Qtde"].sum(), "Valor Recuperado" : ut.formatarMoedaReal(df_loteamento_tipo["Total"].sum())}            
            #df_loteamento_tipo = df_loteamento_tipo.drop("Total", axis=1)            
            #Tabela
            df_loteamento_tipo.loc[len(df_loteamento_tipo)] = row_df
            r_ap3[0].dataframe(df_loteamento_tipo[["Tipo","Qtde","Valor Recuperado"]], hide_index=True)        
            #r_ap3[0].info(f'Total geral....: Quantidade: {df_loteamento_tipo_quantidade_total}    Valor: {ut.formatarMoedaReal(df_loteamento_tipo_total)}')
            
            
            #Loteamento por status virtua
            if not df_loteamento_statusvirtua_aux.empty:                        
                df_loteamento_statusvirtua = pd.merge(df_loteamento_statusvirtua_aux, df_loteamento_recuperado, on="Loteamento")
                df_loteamento_statusvirtua["Valor de Inadimplência"] = df_loteamento_statusvirtua_aux["TotalInadimplencia"].apply(lambda x: ut.formatarMoedaReal(x))
                df_loteamento_statusvirtua["% Recuperada"] = (df_loteamento_statusvirtua["Total"] / df_loteamento_statusvirtua["TotalInadimplencia"]) *100
                df_loteamento_statusvirtua["% Recuperada"] = df_loteamento_statusvirtua["% Recuperada"].apply(lambda x: ut.formatarPorcentagem(x))
                
                #df_loteamento_statusvirtua_totalQtde = df_loteamento_statusvirtua["Qtde"].sum()
                #df_loteamento_statusvirtua_totalValor = df_loteamento_statusvirtua["TotalInadimplencia"].sum()
                row_df ={"Loteamento" :"Total geral", "Qtde" : df_loteamento_statusvirtua["Qtde"].sum(),  "Valor de Inadimplência" : ut.formatarMoedaReal(df_loteamento_statusvirtua["TotalInadimplencia"].sum())}            
                
                #df_loteamento_recuperado = df_loteamento_recuperado.drop("Total", axis=1)
                df_loteamento_statusvirtua = df_loteamento_statusvirtua.drop("Total", axis=1)
                df_loteamento_statusvirtua = df_loteamento_statusvirtua.drop("Valor Recuperado", axis=1)
                #df_loteamento_statusvirtua = df_loteamento_statusvirtua.drop("TotalInadimplencia", axis=1)
                                
                #Grafico Loteamento por valor recuperado
                r_ap2[1].container(height=altura+80).plotly_chart(fig_loteamento_recuperado, use_container_with=True)                
                #Tabela Loteamento por valor recuperado
                df_loteamento_recuperado.loc[len(df_loteamento_recuperado)] = row_df_recuperado
                r_ap2[0].container(height=altura+80).dataframe(df_loteamento_recuperado[["Loteamento","Valor Recuperado"]], hide_index=True, width=altura+80)
                
                #Tabela Loteamento por valor recuperado
                df_loteamento_statusvirtua.loc[len(df_loteamento_statusvirtua)] = row_df
                r_ap4[0].container(height=altura+80).dataframe(df_loteamento_statusvirtua[["Loteamento","Qtde","Valor de Inadimplência","% Recuperada"]], hide_index=True, width=altura+120)
                #r_ap4[0].info(f'Total Quantidade: {df_loteamento_statusvirtua_totalQtde} Total Valor  {ut.formatarMoedaReal(df_loteamento_statusvirtua_totalValor)}')
            else:
                r_ap4[0].warning(f"Não há configuração dos status virtua definido para Contratante {gContratante} em {gMes}/{gAno}")            
           
            #Status virtua por total
            df_statusvirtua_quantidade = dbDistribuicao.consultarStatusVirtuaTotal(gContratante)
            #df_statusvirtua_total = df_statusvirtua["Quantidade"].sum()
            row_df ={"Status" :"Total geral", "Quantidade" : df_statusvirtua_quantidade["Quantidade"].sum()}            
            r_ap5[0].container(height=altura+80,).dataframe(df_statusvirtua_quantidade[["Status","Quantidade"]], hide_index=True, width=altura+80)        
            #r_ap5[0].info(f'Total geral: {df_statusvirtua_total}')
            #Grafico
            fig_statusvirtua = px.bar(df_statusvirtua_quantidade.sort_values("Quantidade", ascending=True),
                                                x="Quantidade", 
                                                y="Status", 
                                                title="Quantidade por Status Virtua", 
                                                orientation="h",
                                                text_auto='.2s')
            fig_statusvirtua.update_traces(textangle=0, textposition="outside")
        
            #colours = ['#5463FF', '#FFC300', '#79b159']
            #fig_forma_convenio_faturamento.update_traces(marker={'colors': colours})        
            r_ap5[1].container(height=altura+80).plotly_chart(fig_statusvirtua, use_container_with=True)
        

        with tab_configuracao:
            st.write(f"Selecione os Status Virtua para referente ao período {gMes}/{gAno}")
            df_tipos_statusvirtua = dbDistribuicao.consultarStatusVirtuaDistintos(gContratante)
            df_configuracoes = dbConfiguracao.consultar(gContratante, gAno, gMes)
            df_configuracao = df_configuracoes[df_configuracoes["ConfChave"] == "status"]
            selecionados = st.multiselect('',
                df_tipos_statusvirtua,
                df_configuracao["ConfValor"],
                placeholder='Selecione...')
            if st.button("Salvar Configurações", type="secondary"):
                objConfig = ent.Configuracao()
                df_configuracaoResultado = objConfig.criarDFStatus(gContratante, gAno, gMes, selecionados)
                if dbConfiguracao.importar(df_configuracaoResultado):
                    st.success("Configurações salvas com sucesso")
                else:
                    st.error("Falha ao Salvar as Configurações")
            df_aux = df_configuracoes[df_configuracoes["ConfChave"] == "sms"]                    
            gSms = int(0) if df_aux.empty else df_aux["ConfValor"].unique()

            gSms = st.number_input("Quantidade de SMS", value=int(gSms), placeholder="Informe a quantidade...")        
            
            df_aux = df_configuracoes[df_configuracoes["ConfChave"] == "ligacao"]
            gLigacao= int(0) if df_aux.empty else df_aux["ConfValor"].unique()
            gLigacao = st.number_input("Quantidade de Ligações", value=int(gLigacao), placeholder="Informe a quantidade...")        
            
            if st.button("Salvar Quantidade", type="secondary"):
                objConfig = ent.Configuracao()
                df_configuracaoResultado = objConfig.criarDFQuantidade(gContratante, gAno, gMes, gSms, gLigacao)
                if dbConfiguracao.importar(df_configuracaoResultado):
                    st.success("Quantidades salvas com sucesso")
                else:
                    st.error("Falha ao Salvar os dados de quantidade")
                                    
     

        with tab_dados:
            r_da1 = st.columns(1)
            r_da2 = st.columns(1)
            
            r_da1[0].write("Dados de Pagamento")
            r_da1[0].dataframe(df_dados_pagamento)
            r_da2[0].write("Dados de Distribuição")
            r_da2[0].dataframe(df_dados_distribuicao)
            
    if st.sidebar.button("Gerar Apresentação", disabled=df_loteamento_statusvirtua_aux.empty):
        objApresentacaoExcel = ent.ApresentacaoExcel(gContratante, 
                                                     int(gAno), 
                                                     int(gMes), 
                                                     df_loteamento_caixa, 
                                                     df_loteamento_recuperado,
                                                     df_loteamento_tipo,
                                                     df_loteamento_statusvirtua,
                                                     df_statusvirtua_quantidade,
                                                     int(gSms),
                                                     int(gLigacao),
                                                     fig_loteamento_caixa)
        try:
            objApresentacaoExcel.gerarPeloTemplate()            
            st.sidebar.success("Arquivo gerado com sucesso")
        except Exception as e:
             st.sidebar.error(f"Falha no geração do arquivo de Apresentação: {e}")
        

       