from dataclasses import dataclass
from controller import CTLPagamento 
import plotly_express as px    
from entity import Contratante as entCon
from entity import ApresentacaoView as entView
from utils import utilidades as ut
from view import ViewBase as vw

@dataclass
class ViewLoteamentoCaixa(vw.ViewBase):
    
    def criar(self, contratante: entCon.Contratante, secao, altura: int):
        
        df_loteamento_caixa = CTLPagamento.consultarLoteamentoValorPago(contratante)
        df_loteamento_caixa["Valor em Caixa"] = df_loteamento_caixa["Total"].apply(lambda x: ut.formatarMoedaReal(x))            
        row_df ={"Loteamento" :"Total geral", "Valor em Caixa" : ut.formatarMoedaReal(df_loteamento_caixa["Total"].sum())}                
                    
        fig_loteamento_caixa = px.pie(df_loteamento_caixa, values='Total', names='Loteamento',
                                        labels={"Total":"Valor em Caixa"},
                                    title='Loteamento por Valor em Caixa', opacity=0.80)
        fig_loteamento_caixa.update_traces(textinfo='percent')
        #df_loteamento_caixa = df_loteamento_caixa.drop("Total", axis=1)
        
        #Grafico
        secao[1].container(height=altura+80).plotly_chart(fig_loteamento_caixa, use_container_with=True)
        
        #Tabela
        df_loteamento_caixa.loc[len(df_loteamento_caixa)] = row_df
        secao[0].container(height=altura+80).dataframe(df_loteamento_caixa[["Loteamento","Valor em Caixa"]], hide_index=True, use_container_width=True )            
        #r_ap1[0].info(f'Total geral: {ut.formatarMoedaReal(df_loteamento_caixa_total)}')
        self.criarView(df_loteamento_caixa, fig_loteamento_caixa)
        

        
        