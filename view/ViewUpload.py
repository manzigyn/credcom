from dataclasses import dataclass
import streamlit as st
from controller import CTLDadosArquivoExcel
from view import ViewImportarArquivoExcel as vwArqExcel

@dataclass
class ViewUpload():

    def criar(self):
        
        languages = {
            "BR": {
                "button": "Buscar",
                "instructions": "Arraste planilhas aqui",
                "limits": "Limite de 200MB por planilha",
            },
        }

        hide_label = (
            """
        <style>
            div[data-testid="stFileUploader"]>section[data-testid="stFileUploadDropzone"]>button[data-testid="baseButton-secondary"] {
            color:white;
            }
            div[data-testid="stFileUploader"]>section[data-testid="stFileUploadDropzone"]>button[data-testid="baseButton-secondary"]::after {
                content: "BUTTON_TEXT";
                color:black;
                display: block;
                position: absolute;
            }
            div[data-testid="stFileDropzoneInstructions"]>div>span {
            visibility:hidden;
            }
            div[data-testid="stFileDropzoneInstructions"]>div>span::after {
            content:"INSTRUCTIONS_TEXT";
            visibility:visible;
            display:block;
            }
            div[data-testid="stFileDropzoneInstructions"]>div>small {
            visibility:hidden;
            }
            div[data-testid="stFileDropzoneInstructions"]>div>small::before {
            content:"FILE_LIMITS";
            visibility:visible;
            display:block;
            }
        </style>
        """.replace(
                "BUTTON_TEXT", languages.get("BR").get("button")
            )
            .replace("INSTRUCTIONS_TEXT", languages.get("BR").get("instructions"))
            .replace("FILE_LIMITS", languages.get("BR").get("limits"))
        )

        st.markdown(hide_label, unsafe_allow_html=True)
        arquivosCarregados = st.file_uploader("Carregar planilhas", accept_multiple_files=True, type=["xlsx"])
        for arquivo in arquivosCarregados:
            bytes_data = arquivo.read()
            #st.write("Planilha:", arquivo.name)
            #st.write(bytes_data)
            
        ctlDadosArquivoExcel = vwArqExcel.ViewImportarArquivoExcel().criar(arquivosCarregados)
        if ctlDadosArquivoExcel.arquivosExcelImportados:
            st.dataframe(ctlDadosArquivoExcel.arquivosExcelImportados, hide_index=True)
        
        