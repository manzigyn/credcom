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
            if obj.ParChave == enPa.EnumParametrizacao.DIR_DADOS:
                self.dir_dados = obj.ParChave
            if obj.ParChave == enPa.EnumParametrizacao.DIR_PROCESSADOS:
                self.dir_processados = obj.ParChave
            if obj.ParChave == enPa.EnumParametrizacao.DIR_TEMPLATE:
                self.dir_template = obj.ParChave
            if obj.ParChave == enPa.EnumParametrizacao.DIR_APRESENTACAO:
                self.dir_apresentacao = obj.ParChave
    