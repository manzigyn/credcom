import streamlit as st
from utils import utilidades as ut
from view import ViewApresentacao as vwApr

st.title("Apresentações")
ut.adicionar_logo('img/logo.png')

viewApresentacao = vwApr.ViewApresentacao()

viewApresentacao.criar()

