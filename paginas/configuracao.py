import streamlit as st
from model import DBParametrizacao  as db
from dto import DTOParametrizacao as dt
from entity import Parametrizacao as entPa
from dataframe import DFParametrizacao as dfPa
from controller import CTLParametrizacao


st.title("Parametrização")

objParametrizacao = CTLParametrizacao.carregar()

with st.form(key="frmParametrizacao"):
    txt_dir_dados = st.text_input(label="Diretório dos arquivos pagamento e distribuição", value=objParametrizacao.dir_dados)
    txt_dir_processados = st.text_input(label="Diretório dos arquivos processados", value=objParametrizacao.dir_processados) 
    txt_dir_template = st.text_input(label="Diretório dos arquivos template para a apresentação", value=objParametrizacao.dir_template) 
    txt_dir_apresentacao = st.text_input(label="Diretório dos arquivos de apresentação gerados", value=objParametrizacao.dir_apresentacao) 
    
    btnSalvar = st.form_submit_button("Salvar")
    
    if btnSalvar:

        msgErro = "sem permissão de escrita ou inexistente"                
        if not CTLParametrizacao.validarPermissaoEscrita(txt_dir_dados):
            st.error(f"Diretório dos arquivos pagamento e distribuição {msgErro}")
        elif not CTLParametrizacao.validarPermissaoEscrita(txt_dir_processados):
            st.error(f"Diretório dos arquivos processados sem permissão de escrita {msgErro}")
        elif not CTLParametrizacao.validarPermissaoEscrita(txt_dir_template):
            st.error(f"Diretório dos arquivos template para a apresentação sem permissão de escrita {msgErro}")
        elif not CTLParametrizacao.validarPermissaoEscrita(txt_dir_apresentacao):
            st.error(f"Diretório dos arquivos de apresentação gerados sem permissão de escrita {msgErro}")            
        else:
            objParametrizacao.criar(txt_dir_dados, txt_dir_processados, txt_dir_template, txt_dir_apresentacao)
            CTLParametrizacao.salvar(objParametrizacao)
            st.success("Parametrização salva com sucesso!")