from st_pages import Page, show_pages, add_page_title
import streamlit as st

show_pages(
    [
        Page("pages/resultado.py", "Resultados", ":chart_with_upwards_trend:"),
        Page("pages/parametrizacao.py","Parametrização",":clipboard:"),
        Page("pages/apresentacao.py","Apresentações",":bar_chart:"),
        Page("pages/upload.py","Arquivos",":open_file_folder:")
    ]
)

#if 'authentication_status' not in ss:
#    st.switch_page('./pages/conta_usuario.py')
    
#MenuButtons(get_roles())
#st.header('Principal')  

#if ss.authentication_status:
#    st.write('Esse conteúdo é acessível para usuários autorizados.')
#else:
#    st.write('Favor realizar o acesso.')  

#login https://github.com/mkhorasani/Streamlit-Authenticator
#https://www.youtube.com/watch?v=dlAjSvrjHeU

#ul.set_png_as_page_bg('img/background.jpeg')  

#Carregar os arquivos de entrada



            

    
