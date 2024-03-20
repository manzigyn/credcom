import datetime
import os
import shutil
import base64
import string
import streamlit as st
import time

global MESES_NOME
MESES_NOME = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

def moverListaArquivos(pasta_origem, pasta_destino, lista):
    for arquivo in lista:
        if not os.path.isfile(arquivo):
            origem = f'{pasta_origem}{arquivo}'
        else:
            origem = arquivo
            
        destino = arquivo.replace(pasta_origem, pasta_destino)
        try:
            shutil.move(origem, destino)
        except FileNotFoundError as error:
            print(f'{error}')
            
def moverArquivo(pasta_origem, pasta_destino, arquivo):
    if not os.path.isfile(arquivo):
        origem = f'{pasta_origem}{arquivo}'
    else:
        origem = arquivo
        
    destino = arquivo.replace(pasta_origem, pasta_destino)
    try:
        shutil.move(origem, destino)
    except FileNotFoundError as error:
        print(f'{error}')
        
def copiarArquivo(origem, destino):
    if os.path.isfile(origem):
        try:
            shutil.copyfile(origem, destino)
        except FileNotFoundError as error:
            print(f'{error}')        
        
def formatarMoedaReal(valor):
    return 'R$ {:,.2f}'.format(valor).replace(",", "X").replace(".", ",").replace("X", ".")

def formatarPorcentagem(valor):
    return '{:,.2f}%'.format(valor).replace(",", "X").replace(".", ",").replace("X", ".")



@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

def obterDataHoraCriacao(arquivo) -> string:
    try:
        ti_c = os.path.getctime(arquivo)
        return time.ctime(ti_c)
    except OSError:
        return datetime.now(tz=None)

def obterDataHoraModificacao(arquivo) -> string:
    try:
        ti_c = os.path.getmtime(arquivo)
        return time.ctime(ti_c)
    except OSError:
        return datetime.now(tz=None)
    
def obterNomeArquivo(arquivo) -> string:
    return os.path.basename(arquivo) if os.path.exists(arquivo) else ''

def formatarArquivoDataCriacao(arquivo) -> string:
    return f'{obterNomeArquivo(arquivo)} {obterDataHoraCriacao(arquivo)}'

def formatarArquivoDataModificacao(arquivo) -> string:
    return f'{obterNomeArquivo(arquivo)} {obterDataHoraModificacao(arquivo)}'

def tratarMoedaReal(valor: str)-> string:
    return valor.replace("R$","").replace(",",".").replace(" ","")