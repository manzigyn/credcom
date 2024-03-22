import pandas as pd
from utils import utilidades as ut
from model import DBConfiguracaoResultado as dbConf
from controller import CTLPagamento 
from controller import CTLDistribuicao
from entity import ApresentacaoResultado as entApre
from entity import Contratante as entCon
from enums import EnumConfiguracaoResultado as enConfig


def obter(contratante: entCon.Contratante) -> entApre.ApresentacaoResultado:
    apresentacaoResultado = entApre.ApresentacaoResultado()
    apresentacaoResultado.contratante = contratante
    apresentacaoResultado.df_pagamento = CTLPagamento.consultarContratante(contratante.nome)
    apresentacaoResultado.df_distribuicao = CTLDistribuicao.consultarContratante(contratante.nome)
    apresentacaoResultado.anos = CTLPagamento.obterListaAno(apresentacaoResultado.df_pagamento)
    apresentacaoResultado.meses = CTLPagamento.obterListaMes(apresentacaoResultado.df_pagamento)
    return apresentacaoResultado