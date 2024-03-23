import streamlit as st
from controller import CTLParametrizacao
from utils import utilidades as ut

st.title("Parametrização")
ut.adicionar_logo('img/logo.png')

ctlParametrizacao = CTLParametrizacao.carregar()

with st.form(key="frmParametrizacao"):
    txt_dir_dados = st.text_input(label="Diretório dos arquivos pagamento e distribuição", value=ctlParametrizacao.dir_dados)
    txt_dir_processados = st.text_input(label="Diretório dos arquivos processados", value=ctlParametrizacao.dir_processados) 
    txt_dir_template = st.text_input(label="Diretório dos arquivos template para a apresentação", value=ctlParametrizacao.dir_template) 
    txt_dir_apresentacao = st.text_input(label="Diretório dos arquivos de apresentação gerados", value=ctlParametrizacao.dir_apresentacao) 
    
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
            ctlParametrizacao.criar(txt_dir_dados, txt_dir_processados, txt_dir_template, txt_dir_apresentacao)
            CTLParametrizacao.salvar(ctlParametrizacao)
            st.success("Parametrização salva com sucesso!")