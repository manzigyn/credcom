
import pandas as pd
from utils import utilidades as ut
from model import DBConfiguracaoResultado as dbConf
from model import DBDistribuicao as dbDis
from entity import ConfiguracaoResultado as entConfig
from entity import Contratante as entCon
from enums import EnumConfiguracaoResultado as enConfig


def criarDFStatus(configuracao: entConfig.ConfiguracaoResultado, todoAno=False):
    inicio = configuracao.contratante.mes
    fim = configuracao.contratante.mes
    if todoAno:
        inicio =1
        fim = 12
    df_result = pd.DataFrame(columns=['ConfContratante','ConfAno','ConfMes','ConfChave','ConfValor'])            
    for mes_corrente in range(inicio, fim+1):
        df_saida = pd.DataFrame(columns=['ConfContratante','ConfAno','ConfMes','ConfChave','ConfValor'])
        df_saida["ConfValor"] = configuracao.status
        df_saida["ConfContratante"] = configuracao.contratante.nome
        df_saida["ConfAno"] = int(configuracao.contratante.ano)
        df_saida["ConfMes"] = int(mes_corrente)
        df_saida["ConfChave"]= enConfig.EnumConfiguracaoResultado.STATUS
        df_result = pd.concat([df_result, df_saida], ignore_index=True)
    return df_result

def criarDFQuantidade(configuracao: entConfig.ConfiguracaoResultado):
    dados = {'ConfContratante': [configuracao.contratante.nome, configuracao.contratante.nome],
                'ConfAno': [int(configuracao.contratante.ano), int(configuracao.contratante.ano)],
                'ConfMes': [int(configuracao.contratante.mes), int(configuracao.contratante.mes)],
                'ConfChave': [enConfig.EnumConfiguracaoResultado.SMS, enConfig.EnumConfiguracaoResultado.LIGACAO], 
                'ConfValor': [int(configuracao.sms), int(configuracao.ligacao)]}        
    
    return pd.DataFrame(data=dados)

def criarDFUnico(contratante: entCon.Contratante, chave, valor)-> pd.DataFrame:
    df = {'ConfContratante': [contratante.nome], 
            'ConfAno': [int(contratante.ano)], 
            'ConfMes': [int(contratante.mes)], 
            'ConfChave': [chave], 
            'ConfValor': [valor]}
    return pd.DataFrame(df)

def replicar(contratante: entCon.Contratante):
    dbConfiguracao = dbConf.DBConfiguracaoResultado()
    df = dbConfiguracao.consultar(contratante)
    df_saida = criarDFStatus(contratante,  df["ConfValor"])
    return df_saida

def salvarStatus(configuracao: entConfig.ConfiguracaoResultado, todoAno=False) -> bool:
    df_configuracao = criarDFStatus(configuracao, todoAno)
    return dbConf.DBConfiguracaoResultado().salvar(df_configuracao)

def salvarQuantidade(configuracao: entConfig.ConfiguracaoResultado) -> bool:
    df_configuracao = criarDFQuantidade(configuracao)
    return dbConf.DBConfiguracaoResultado().salvar(df_configuracao)

def obter(contratante: entCon.Contratante) -> entConfig.ConfiguracaoResultado:
    configuracaoResultado = entConfig.ConfiguracaoResultado()
    configuracaoResultado.contratante = contratante
    configuracaoResultado.statusVirtua = dbDis.DBDistribuicao().consultarStatusVirtuaDistintos(contratante.nome)
    
    dbConfiguracao = dbConf.DBConfiguracaoResultado()    
    df_configuracoes = dbConfiguracao.consultar(contratante)
    
    df_configuracao = df_configuracoes[df_configuracoes["ConfChave"] == enConfig.EnumConfiguracaoResultado.STATUS]
    configuracaoResultado.status = df_configuracao["ConfValor"]
    
    df_configuracao = df_configuracoes[df_configuracoes["ConfChave"] == enConfig.EnumConfiguracaoResultado.SMS]
    configuracaoResultado.sms = int(df_configuracao["ConfValor"].unique()) if not df_configuracao["ConfValor"].isna else 0
    
    df_configuracao = df_configuracoes[df_configuracoes["ConfChave"] == enConfig.EnumConfiguracaoResultado.LIGACAO]
    configuracaoResultado.ligacao = int(df_configuracao["ConfValor"].unique()) if not df_configuracao["ConfValor"].isna else 0
    return configuracaoResultado
