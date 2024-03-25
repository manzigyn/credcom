from dataclasses import dataclass
from controller import CTLPagamento 
import plotly_express as px    
from entity import Contratante as entCon
from entity import ApresentacaoView as entView
from utils import utilidades as ut
from view import ViewBase as vw
import streamlit as st
from io import StringIO, BytesIO
import base64

@dataclass
class ViewLoteamentoCaixa(vw.ViewBase):
    
    def criar(self, contratante: entCon.Contratante, secao, altura: int):
        
        df_loteamento_caixa = CTLPagamento.consultarLoteamentoValorPago(contratante)
        df_loteamento_caixa["Valor em Caixa"] = df_loteamento_caixa["Total"].apply(lambda x: ut.formatarMoedaReal(x))            
        self.df_resumo ={"Loteamento" :"Total geral", "Valor em Caixa" : ut.formatarMoedaReal(df_loteamento_caixa["Total"].sum())}                
                    
        fig_loteamento_caixa = px.pie(df_loteamento_caixa, values='Total', names='Loteamento',
                                        labels={"Total":"Valor em Caixa"},
                                    title='Loteamento por Valor em Caixa', opacity=0.80)
        fig_loteamento_caixa.update_traces(textinfo='label+percent')
        fig_loteamento_caixa.update(layout_showlegend=False)
        #df_loteamento_caixa = df_loteamento_caixa.drop("Total", axis=1)
        #fig_loteamento_caixa.write_image("dados/apresentacao/loteamento.png")
        #mybuff = StringIO()
        #fig_loteamento_caixa.write_html(mybuff, include_plotlyjs='cdn')
        #mybuff = BytesIO(mybuff.getvalue().encode())
        #b64 = base64.b64encode(mybuff.read()).decode()
        #href = f'<a href="data:text/html;charset=utf-8;base64, {b64}" download="plot.html">Download plot</a>'
        #st.markdown(href, unsafe_allow_html=True)
        #Grafico
        secao[1].container(height=altura+80).plotly_chart(fig_loteamento_caixa, use_container_with=True)
        
        #Tabela
        df_loteamento_caixa.loc[len(df_loteamento_caixa)] = self.df_resumo
        #df_loteamento_caixa.style.set_properties(**{"font-weight": "bold"}, subset=["Loteamento","Valor em Caixa"])
        secao[0].container(height=altura+80).dataframe(df_loteamento_caixa[["Loteamento","Valor em Caixa"]], hide_index=True, use_container_width=True )            
       
        self.criarView(df_loteamento_caixa, fig_loteamento_caixa)
    
        
        

        
        