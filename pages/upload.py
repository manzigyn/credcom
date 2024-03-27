import streamlit as st
from view import ViewUpload as vwUp
from utils import utilidades as ut

st.title("Planilhas de Pagamentos e Distribuição")
ut.adicionar_logo('img/logo.png')

viewUpload = vwUp.ViewUpload()
viewUpload.criar()
