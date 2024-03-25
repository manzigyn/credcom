from dataclasses import dataclass
from dataclasses import field
import streamlit as st
from controller import CTLConfiguracaoResultado
from entity import Contratante as entCont
from entity import ConfiguracaoResultado as entConfig

@dataclass
class ViewParametrizacao():
    
    configuracaoResultado : entConfig.ConfiguracaoResultado = field(default_factory=entConfig.ConfiguracaoResultado)
    
    def criar(self, contratante: entCont.Contratante):
        st.write(f"Selecione os Status Virtua para referente ao período {contratante.mes}/{contratante.ano}")
        entConfiguracaoResultado = CTLConfiguracaoResultado.obter(contratante)
        cmbSelecionados = st.multiselect('',
            entConfiguracaoResultado.statusVirtua,
            entConfiguracaoResultado.status,
            placeholder='Selecione...',
            label_visibility='collapsed')
        chkTodoAno = st.checkbox(f"Aplicar para todos os meses de {contratante.ano}")
        
        if st.button("Salvar Status", type="secondary"):
            entConfiguracaoResultado.status = cmbSelecionados
            if CTLConfiguracaoResultado.salvarStatus(entConfiguracaoResultado, chkTodoAno):
                st.success("Configurações salvas com sucesso")
            else:
                st.error("Falha ao Salvar as Configurações")


        sms = st.number_input("Quantidade de SMS", value=entConfiguracaoResultado.sms, placeholder="Informe a quantidade...")                    
        ligacao = st.number_input("Quantidade de Ligações", value=entConfiguracaoResultado.ligacao, placeholder="Informe a quantidade...")        
        
        entConfiguracaoResultado.sms = sms
        entConfiguracaoResultado.ligacao = ligacao

        self.configuracaoResultado = entConfiguracaoResultado
        if st.button("Salvar Quantidade", type="secondary"):
            if CTLConfiguracaoResultado.salvarQuantidade(entConfiguracaoResultado):
                st.success("Quantidades salvas com sucesso")
            else:
                st.error("Falha ao Salvar os dados de quantidade")