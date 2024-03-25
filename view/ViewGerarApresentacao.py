from dataclasses import dataclass
import streamlit as st
from controller import CTLGerarApresentacao as ctlAp
from entity import ApresentacaoExcel as entAp

@dataclass
class ViewGerarApresentacao():
    
    def criar(self, apresentacaoExcel: entAp.ApresentacaoExcel, desabilitaBotao: bool):

        ctlApresentacaoExcel = ctlAp.CTLApresentacaoExcel(apresentacaoExcel)
        desabilitaBotao = desabilitaBotao or not ctlApresentacaoExcel.parametrizacao.haGeracao()
       
        if st.sidebar.button("Gerar Apresentação", disabled= desabilitaBotao):
            try:
                excel = ctlApresentacaoExcel.gerarPeloTemplate() 
                if excel :    
                    st.sidebar.success("Arquivo gerado com sucesso")      
            
                    if apresentacaoExcel.caminhoArquivo:
                        with open(apresentacaoExcel.caminhoArquivo, "rb") as template_file:
                            template_byte = template_file.read()

                            st.sidebar.download_button(label="Download",
                                                data=template_byte,
                                                file_name= apresentacaoExcel.nomeArquivo ,
                                                mime='application/octet-stream')
                else:
                    st.sidebar.warning("Não foi possível gerar a apresentação devido a falta do template")      
            except Exception as e:
                st.sidebar.error(f"Falha no geração do arquivo de Apresentação: {e}")
                
        if desabilitaBotao:
            st.sidebar.warning("Falta definir a parametrização para os dados selecionados")