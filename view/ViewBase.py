from dataclasses import dataclass
from dataclasses import field
import pandas as pd
from matplotlib.figure import Figure
from entity import ApresentacaoView as entView

@dataclass
class ViewBase():
    apresentacaoView : entView.ApresentacaoView = field(default_factory =entView.ApresentacaoView)
    df_resumo: pd.DataFrame = field(default_factory=pd.DataFrame)
    
    def criarView(self, tabela: pd.DataFrame, grafico: Figure):
        self.apresentacaoView.df_tabela = tabela
        self.apresentacaoView.grafico = grafico
        return self.apresentacaoView
    
    def inserirResumo(self):
        self.apresentacaoView.df_tabela.loc[len(self.apresentacaoView.df_tabela)] = self.df_resumo