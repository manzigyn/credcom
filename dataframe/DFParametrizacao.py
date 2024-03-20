from dataclasses import dataclass
import pandas as pd
from enums import EnumParametrizacao as ep
from entity import Parametrizacao as pa


@dataclass
class DFParametrizacao():
    def criarDF(self, parametrizacao: pa.Parametrizacao):
        enum = ep.EnumParametrizacao
        dados = {'ParChave': [enum.DIR_DADOS, enum.DIR_PROCESSADOS, enum.DIR_TEMPLATE, enum.DIR_APRESENTACAO],
                    'ParValor': [parametrizacao.dir_dados, parametrizacao.dir_processados, parametrizacao.dir_template, parametrizacao.dir_apresentacao]
                }        
        
        return pd.DataFrame(data=dados)
