from dataclasses import dataclass
from controller import CTLPagamento 
from entity import Contratante as entCon
from utils import utilidades as ut
from view import ViewBase as vw

@dataclass
class ViewLoteamentoTipo(vw.ViewBase):
    
    def criar(self, contratante: entCon.Contratante, secao, altura: int):
        df_loteamento_tipo = CTLPagamento.consultarTipoNegociacao(contratante)
        df_loteamento_tipo["Valor Recuperado"] = df_loteamento_tipo["Total"].apply(lambda x: ut.formatarMoedaReal(x))
        
        self.df_resumo ={"Tipo" :"Total geral","Qtde" : df_loteamento_tipo["Qtde"].sum(), "Valor Recuperado" : ut.formatarMoedaReal(df_loteamento_tipo["Total"].sum())}            

        #Tabela
        df_loteamento_tipo.loc[len(df_loteamento_tipo)] = self.df_resumo
        secao[0].container(height=altura+80).dataframe(df_loteamento_tipo[["Tipo","Qtde","Valor Recuperado"]], hide_index=True, use_container_width=True)        
        
        self.criarView(df_loteamento_tipo, None)                   