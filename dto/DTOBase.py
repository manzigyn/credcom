from typing import TypedDict
import pandas as pd
from dataclasses import dataclass

@dataclass
class DTOBase:
    lista: list = []
    
    def loadDF(self, df: pd.DataFrame):
        self.lista = [DTOBase(**kwargs) for kwargs in df.to_dict(orient='records')]