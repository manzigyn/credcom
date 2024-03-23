from dataclasses import dataclass
from controller import CTLDistribuicao
from entity import Contratante as entCon
from utils import utilidades as ut
from view import ViewBase as vw
import pandas as pd

@dataclass
class ViewLoteamentoStatusVirtua(vw.ViewBase):    

    def inicializar(self, contratante: entCon.Contratante):
        self.apresentacaoView.df_tabela_aux = CTLDistribuicao.consultarLoteamentoValorTotal(contratante)
        
    def haStatus(self):
        return not self.apresentacaoView.df_tabela_aux.empty
    
    def criar(self, secao, altura: int,  df_loteamento_recuperado: pd.DataFrame):
        df_loteamento_statusvirtua = pd.merge(self.apresentacaoView.df_tabela_aux, df_loteamento_recuperado, how="left", on="Loteamento")
        df_loteamento_statusvirtua["Valor de Inadimplência"] = df_loteamento_statusvirtua["TotalInadimplencia"].apply(lambda x: ut.formatarMoedaReal(x))
        df_loteamento_statusvirtua["% Recuperada"] = (df_loteamento_statusvirtua["Total"] / df_loteamento_statusvirtua["TotalInadimplencia"]) *100
        df_loteamento_statusvirtua["% Recuperada"] = df_loteamento_statusvirtua["% Recuperada"].apply(lambda x: ut.formatarPorcentagem(x))
        
        total_porcentagem = ut.formatarPorcentagem((df_loteamento_recuperado["Total"].sum() / df_loteamento_statusvirtua["TotalInadimplencia"].sum()) * 100)
        self.df_resumo ={"Loteamento" :"Total geral", "Qtde" : df_loteamento_statusvirtua["Qtde"].sum(),  "Valor de Inadimplência" : ut.formatarMoedaReal(df_loteamento_statusvirtua["TotalInadimplencia"].sum()), "% Recuperada" : total_porcentagem}            
        
        df_loteamento_statusvirtua = df_loteamento_statusvirtua.drop("Total", axis=1)
        df_loteamento_statusvirtua = df_loteamento_statusvirtua.drop("Valor Recuperado", axis=1)

        #Tabela Loteamento por valor recuperado
        df_loteamento_statusvirtua.loc[len(df_loteamento_statusvirtua)] = self.df_resumo
        secao[1].container(height=altura+80).dataframe(df_loteamento_statusvirtua[["Loteamento","Qtde","Valor de Inadimplência","% Recuperada"]], hide_index=True, use_container_width=True)
        
        self.criarView(df_loteamento_statusvirtua, None)