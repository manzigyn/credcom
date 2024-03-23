from dataclasses import dataclass
import streamlit as st
from controller import CTLDadosArquivoExcel as ctlArqExc
import traceback

@dataclass
class ViewDadosArquivoExcel():
    
    def criar(self):
        ctlDadosArquivoExcel = ctlArqExc.DadosArquivoExcel()

        if ctlDadosArquivoExcel.haNovosArquivos():
            st.warning(f'Pagamento {len(ctlDadosArquivoExcel.lista_pagamento)} Distribuição: {len(ctlDadosArquivoExcel.lista_distribuicao)}')
            if st.button('Atualizar Arquivos',type='primary'):
                try:
                    ctlDadosArquivoExcel.processarArquivos()
                    st.success("Arquivos atualizados com sucesso")
                except Exception as e:
                    mensagem = traceback.format_exc()
                    with st.expander('Falha no processamento do arquivo'):
                        st.markdown(mensagem)
    