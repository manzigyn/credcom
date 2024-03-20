from dto import DTOBase as dt
from dataclasses import dataclass

@dataclass
class DTOParametrizacao(dt.DTOBase):
    chave: str = ''
    valor: str = ''
    
