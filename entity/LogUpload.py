from dataclasses import dataclass
from dataclasses import field
from enums import EnumTipoArquivoExcel as enTipo
from datetime import datetime

@dataclass
class LogUpload():
    Nome: str = ''
    Tipo: enTipo.EnumTipoArquivoExcel = field(default_factory=enTipo.EnumTipoArquivoExcel)
    Operador: str = '1'
    Resultado: str = ''
    Processamento: str = datetime.today().strftime('%d/%m/%Y %H:%M:%S')    
   

        
    