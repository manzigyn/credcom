import streamlit as st

st.title("Parametrização")

with st.form(key="frmParametrizacao"):
    txt_dir_dados = st.text_input(label="Diretório dos arquivos pagamento e distribuição")
    txt_dir_processados = st.text_input(label="Diretório dos arquivos processados") 
    txt_dir_template = st.text_input(label="Diretório dos arquivos template para a apresentação") 
    txt_dir_apresentacao = st.text_input(label="Diretório dos arquivos de apresentação gerados") 
    
    btnSalvar = st.form_submit_button("Salvar")
    
    if btnSalvar:
        st.success("Parametrização salva com sucesso!")