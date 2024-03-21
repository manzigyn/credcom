from dataclasses import dataclass
from typing import TypedDict
import pandas as pd
from dto import DTOParametrizacao as dto
from enums import EnumParametrizacao as enPa
from typing import List, TypeVar
from utils import utilidades as ut


@dataclass
class Parametrizacao():
    dir_dados: str = ''
    dir_processados: str = ''
    dir_template: str = ''
    dir_apresentacao: str = ''
    
    def criar(self, dir_dados: str, dir_processados: str, dir_template: str, dir_apresentacao: str):
        self.dir_dados = ut.inserirCaracterFinal(dir_dados,'\\')
        self.dir_processados = ut.inserirCaracterFinal(dir_processados,'\\')
        self.dir_template = ut.inserirCaracterFinal(dir_template, '\\')
        self.dir_apresentacao = ut.inserirCaracterFinal(dir_apresentacao, '\\')
    
    def carregar(self, lista: List[dto.DTOParametrizacao]):
        for obj in lista:
            if obj.ParChave == enPa.EnumParametrizacao.DIR_DADOS:
                self.dir_dados = obj.ParValor
            if obj.ParChave == enPa.EnumParametrizacao.DIR_PROCESSADOS:
                self.dir_processados = obj.ParValor
            if obj.ParChave == enPa.EnumParametrizacao.DIR_TEMPLATE:
                self.dir_template = obj.ParValor
            if obj.ParChave == enPa.EnumParametrizacao.DIR_APRESENTACAO:
                self.dir_apresentacao = obj.ParValor
    