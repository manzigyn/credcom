from dataclasses import dataclass
from controller import CTLPagamento 
import plotly_express as px    
from entity import Contratante as entCon
from utils import utilidades as ut
from view import ViewBase as vw

@dataclass
class ViewLoteamentoRecuperado(vw.ViewBase):
    
    def criar(self, contratante: entCon.Contratante):
        df_loteamento_recuperado = CTLPagamento.consultarLoteamentoValorRecuperado(contratante)
        df_loteamento_recuperado["Valor Recuperado"] = df_loteamento_recuperado["Total"].apply(lambda x: ut.formatarMoedaReal(x))            
        self.df_resumo ={"Loteamento" :"Total geral", "Valor Recuperado" : ut.formatarMoedaReal(df_loteamento_recuperado["Total"].sum())}            
        
        fig_loteamento_recuperado = px.pie(df_loteamento_recuperado, values='Total', names='Loteamento',
                                        labels={"Total":"Valor Recuperado"},
                                    title='Loteamento por Valor Recuperado', opacity=0.80)
        fig_loteamento_recuperado.update_traces(textinfo='percent')
        
        self.criarView(df_loteamento_recuperado, fig_loteamento_recuperado)
        
    def atualizaDados(self, secao, altura: int):
        secao[1].container(height=altura+80).plotly_chart(self.apresentacaoView.grafico, use_container_with=True)   
        self.inserirResumo()
        secao[0].container(height=altura+80).dataframe(self.apresentacaoView.df_tabela[["Loteamento","Valor Recuperado"]], hide_index=True, use_container_width=True)
             
        