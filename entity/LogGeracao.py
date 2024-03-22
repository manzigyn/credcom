from dataclasses import dataclass
from datetime import datetime

@dataclass
class LogGeracao():
    contratante: str = ''
    ano: int = 0
    mes: int = 0
    operador = 1
    data: str = datetime.today().strftime('%Y%m%d:%M:%S')
    horario: str = datetime.today().strftime('%H:%M:%S')
    arquivo: str = ''