from dataclasses import dataclass
from dataclasses import field
import pandas as pd
from matplotlib.figure import Figure

@dataclass
class ApresentacaoView():
    df_tabela: pd.DataFrame = field(default_factory = pd.DataFrame)
    grafico: Figure = field(default_factory = Figure)