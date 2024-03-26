import streamlit as st
from view import ViewParametrizacao as vwPar
from utils import utilidades as ut

st.title("Parametrização")
ut.adicionar_logo('img/logo.png')


viewParametrizacao = vwPar.ViewParametrizacao()
viewParametrizacao.criar()

