import streamlit as st
from database import DBParametrizacao  as db
from dto import DTOParametrizacao as dt
from entity import Parametrizacao as pa
from dataframe import DFParametrizacao as dfPa

st.title("Parametrização")

dbParametrizacao = db.DBParametrizacao()
dtoParametrizacao = dt.DTOParametrizacao()
df = dbParametrizacao.consultarTodos()
dtoParametrizacao.loadDF(df)
obj = pa.Parametrizacao()
obj.load(dtoParametrizacao.lista)


with st.form(key="frmParametrizacao"):
    txt_dir_dados = st.text_input(label="Diretório dos arquivos pagamento e distribuição", value=obj.dir_dados)
    txt_dir_processados = st.text_input(label="Diretório dos arquivos processados", value=obj.dir_processados) 
    txt_dir_template = st.text_input(label="Diretório dos arquivos template para a apresentação", value=obj.dir_template) 
    txt_dir_apresentacao = st.text_input(label="Diretório dos arquivos de apresentação gerados", value=obj.dir_apresentacao) 
    
    btnSalvar = st.form_submit_button("Salvar")
    
    if btnSalvar:
        obj.dir_dados = txt_dir_dados
        obj.dir_processados = txt_dir_processados
        obj.dir_template = txt_dir_template
        obj.dir_apresentacao = txt_dir_apresentacao
        objDf = dfPa.DFParametrizacao()
        df = objDf.criarDF(obj)
        dbParametrizacao.importar(df)
        st.success("Parametrização salva com sucesso!")