import streamlit as st
from dataclasses import dataclass
from entity import Contratante as entCont
from controller import CTLLogGeracao
from controller import CTLPagamento
#from IPython.display import HTML
import requests

@dataclass
class ViewApresentacao():
    
    def criar(self):
        padrao = 'Selecione...'
        df_contratante = CTLPagamento.consultarContratantesDistintos()
        df_logApresentacao = CTLLogGeracao.consultarAnoMesDistinto()

        entContratante = entCont.Contratante()

        entContratante.nome = st.sidebar.selectbox("Contratante", options=[padrao]+list(CTLPagamento.obterListaContratante(df_contratante)))
        entContratante.ano = st.sidebar.selectbox("Ano", options=[padrao]+list(CTLLogGeracao.obterListaAno(df_logApresentacao)))
        entContratante.mes = st.sidebar.selectbox("Mês", options=[padrao]+list(CTLLogGeracao.obterListaMes(df_logApresentacao)))
        chkNaoGerados = st.sidebar.checkbox("Somente não gerados",False)
        
        df_apresentacao = CTLLogGeracao.consultar(entContratante, padrao, chkNaoGerados)
        
        if not df_apresentacao.empty:
        
            df_apresentacao.insert(len(df_apresentacao.columns), "Apresentação", 'Download')

            colms = st.columns((2, 1, 1, 2, 2, 2,2))

            #write headers
            for col, field_name in zip(colms, df_apresentacao[["Contratante","Ano","Mes","Operador","Data","Horario","Apresentação"]].columns):
                col.write(f'**{field_name}**')
            
            #df_apresentacao['Apresentação'] = df_apresentacao['Caminho'].apply(
            #    lambda x: f'<a download="{obterArquivoByte(x)}" href="data:application/octet-stream" target="_blank">Download</a>' if x else '')

            #st.write(HTML(df_apresentacao[["Contratante","Ano","Mes","Operador","Data","Horario","Apresentação"]].to_html(escape=False)), unsafe_allow_html=True)
            df_apresentacao.apply(escreverLinha, axis=1)
        else:
            st.warning("Não há registros para o filtro selecionado.")

def escreverLinha(row):
    col1, col2, col3, col4, col5, col6, col7 = st.columns((2, 1, 1, 2, 2, 2,2))
    with col1:
        st.write(row['Contratante'])
    with col2:
        st.write(str(row['Ano']))
    with col3:
        st.write(str(row['Mes']))
    with col4:
        st.write(row['Operador'] if row['Operador'] else "")
    with col5:
        st.write(row['Data'] if row['Data'] else "")
    with col6:
        st.write(row['Horario'] if row['Horario'] else "")                
    with col7:
        if row['Caminho']:
            st.download_button(label="Download",
                                data=obterArquivoByte(row['Caminho']),
                                file_name= row['Arquivo'] ,
                                mime='application/octet-stream')
        
def obterArquivoByte(caminhoArquivo):
     with open(caminhoArquivo, "rb") as template_file:
        return template_file.read()
        #return requests.get(template_file).content
    
def download_file(url):

    # this will grab the filename from the url
    filename = url.split('/')[-1]

    print(f'Downloading {filename}')

    r = requests.get(url)

    with open(filename, 'wb') as output_file:
        output_file.write(r.content)

    print('ok')    

