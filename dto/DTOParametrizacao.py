from dto import DTOBase as dt
from dataclasses import dataclass
import pandas as pd

@dataclass
class DTOParametrizacao(dt.DTOBase):
    ParChave: str = ''
    ParValor: str = ''
    
    def loadDF(self, df: pd.DataFrame):
        self.lista = [DTOParametrizacao(**kwargs) for kwargs in df.to_dict(orient='records')]