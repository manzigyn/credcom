from dataclasses import dataclass
from dataclasses import field
import pandas as pd
from matplotlib.figure import Figure
from entity import ApresentacaoView as entView

@dataclass
class ViewBase():
    apresentacaoView : entView.ApresentacaoView = field(default_factory =entView.ApresentacaoView)
    
    def criarView(self, tabela: pd.DataFrame, grafico: Figure):
        self.apresentacaoView.df_tabela = tabela
        self.apresentacaoView.grafico = grafico
        return self.apresentacaoView
    
    def inserirResumo(self, df_resumo):
        self.apresentacaoView.loc[len(self.apresentacaoView)] = df_resumo