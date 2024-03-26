from st_pages import Page, show_pages, add_page_title
from sqlalchemy import create_engine
import streamlit as st

show_pages(
    [
        Page("paginas/resultado.py", "Resultados", ":chart_with_upwards_trend:"),
        Page("paginas/parametrizacao.py","Parametrização",":clipboard:"),
        Page("paginas/apresentacao.py","Apresentações",":bar_chart:"),
        Page("paginas/upload.py","Arquivos",":open_file_folder:")
    ]
)

#login https://github.com/mkhorasani/Streamlit-Authenticator
#https://www.youtube.com/watch?v=dlAjSvrjHeU

#ul.set_png_as_page_bg('img/background.jpeg')  

#Carregar os arquivos de entrada



            

    
