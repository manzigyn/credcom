from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from entity import Contratante as entCont

@dataclass
class LogGeracao():
    contratante: entCont.Contratante = field(default_factory=entCont.Contratante)
    operador = 1
    data: str = datetime.today().strftime('%d/%m/%Y')
    horario: str = datetime.today().strftime('%H:%M:%S')
    arquivo: str = ''
    caminho: str = ''
    
    