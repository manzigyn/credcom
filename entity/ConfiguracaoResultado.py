from dataclasses import dataclass
from dataclasses import field
from entity import Contratante as entCont
import pandas as pd

@dataclass
class ConfiguracaoResultado():
    contratante: entCont.Contratante = field(default_factory=entCont.Contratante)
    status: list = field(default_factory=list)
    sms: int = 0
    ligacao: int = 0
    statusVirtua: pd.DataFrame = field(default_factory = pd.DataFrame)