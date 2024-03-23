from dataclasses import dataclass
import plotly_express as px    
from entity import Contratante as entCon
from controller import CTLDistribuicao
from utils import utilidades as ut
from view import ViewBase as vw

@dataclass
class ViewStatusVirtuaQuantidade(vw.ViewBase):
    
     def criar(self, contratante: entCon.Contratante, secao, altura: int):
        df_statusvirtua_quantidade = CTLDistribuicao.consultarStatusVirtuaTotal(contratante)
        self.df_resumo ={"Status" :"Total geral", "Quantidade" : df_statusvirtua_quantidade["Quantidade"].sum()}            
        df_statusvirtua_quantidade.loc[len(df_statusvirtua_quantidade)] = self.df_resumo
        
        #Tabela
        secao[0].container(height=altura+80,).dataframe(df_statusvirtua_quantidade[["Status","Quantidade"]], hide_index=True, use_container_width=True)        

        #Grafico
        fig_statusvirtua = px.bar(df_statusvirtua_quantidade.sort_values("Quantidade", ascending=True),
                                            x="Quantidade", 
                                            y="Status", 
                                            title="Quantidade por Status Virtua", 
                                            orientation="h",
                                            text_auto='.2s')
        fig_statusvirtua.update_traces(textangle=0, textposition="outside")
        secao[1].container(height=altura+80).plotly_chart(fig_statusvirtua, use_container_with=True)
                 
        self.criarView(df_statusvirtua_quantidade, fig_statusvirtua)             