from dataclasses import dataclass
from typing import TypedDict
import pandas as pd
from dto import DTOParametrizacao as dto
from enums import EnumParametrizacao as enPa
from typing import List, TypeVar


@dataclass
class Parametrizacao():
    dir_dados: str = ''
    dir_processados: str = ''
    dir_template: str = ''
    dir_apresentacao: str = ''
    
    def load(self, lista: List[dto.DTOParametrizacao]):
        for obj in lista:
            if obj.chave == enPa.EnumParametrizacao.DIR_DADOS:
                self.dir_dados = obj.chave
            if obj.chave == enPa.EnumParametrizacao.DIR_PROCESSADOS:
                self.dir_processados = obj.chave
            if obj.chave == enPa.EnumParametrizacao.DIR_TEMPLATE:
                self.dir_template = obj.chave
            if obj.chave == enPa.EnumParametrizacao.DIR_APRESENTACAO:
                self.dir_apresentacao = obj.chave
    