from dataclasses import dataclass
from dataclasses import field
from entity import Contratante as entCont
import pandas as pd

@dataclass
class ApresentacaoResultado():
    contratante: entCont.Contratante = field(default_factory=entCont.Contratante)
    anos: list = field(default_factory=list)
    meses: list = field(default_factory=list)
    df_pagamento: pd.DataFrame = field(default_factory = pd.DataFrame)
    df_distribuicao: pd.DataFrame = field(default_factory = pd.DataFrame)