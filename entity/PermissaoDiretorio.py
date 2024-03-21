from dataclasses import dataclass
import os

@dataclass
class PermissaoDiretorio():
    leitura: bool = False
    escrita: bool = False
    execucao: bool = False
        
    def verificarPermissaoDiretorio(self, diretorio):
        permissions = os.stat(diretorio).st_mode
        self.leitura = True if permissions & 0o400 else False
        self.escrita = True if permissions & 0o200  else False
        self.execucao = True if permissions & 0o100  else False