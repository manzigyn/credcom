import streamlit as st
from model import DBParametrizacao  as db
from dto import DTOParametrizacao as dt
from entity import Parametrizacao as entPa
from dataframe import DFParametrizacao as dfPa
from controller import CTLLogGeracao
from utils import utilidades as ut


st.title("Apresentações")
ut.adicionar_logo('img/logo.png')

df_logApresentacao = CTLLogGeracao.consultarContratantesDistintos()

ano = st.sidebar.selectbox("Ano", CTLLogGeracao.obterListaAno(df_logApresentacao))
mes = st.sidebar.selectbox("Mês", CTLLogGeracao.obterListaMes(df_logApresentacao))