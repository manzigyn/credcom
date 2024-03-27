from dataclasses import dataclass
import pandas as pd
import os
from utils import utilidades as ut
from controller import CTLPagamento 
from controller import CTLDistribuicao
from controller import CTLParametrizacao 
from controller import CTLLogUpload
from enums import EnumTipoArquivoExcel as enTipo
from entity import LogUpload as entUpl


@dataclass
class DadosArquivoExcel():
    lista_pagamento = []
    lista_distribuicao = []
    parametrizacao = CTLParametrizacao.carregar()
    pasta = parametrizacao.dir_dados if parametrizacao.dir_dados else 'dados/' 
    processados = parametrizacao.dir_processados if parametrizacao.dir_processados else f'dados/processados/'
    arquivosCarregados = []
    arquivosExcelImportados =[]
    
    def __init__(self, arquivosCarregados, viaUpload: bool=False):
        if not arquivosCarregados and not viaUpload:
            self.listarArquivos()
        else:
            self.arquivosCarregados = arquivosCarregados
            self.arquivosExcelImportados.clear()
            self.listarArquivosCarregados(arquivosCarregados)
    
    def listarArquivos(self):
        self.lista_pagamento.clear()
        self.lista_distribuicao.clear()
        if not os.path.isdir(self.processados):
            os.makedirs(self.processados)

        for arquivo in os.listdir(self.pasta):
            if arquivo.endswith(".xlsx"): 
                origem = f'{self.pasta}{arquivo}'
                if any(x in arquivo for x in [enTipo.EnumTipoArquivoExcel.PAGAMENTO]):
                    self.lista_pagamento.append(origem)            
                elif any(x in arquivo for x in [enTipo.EnumTipoArquivoExcel.DISTRIBUICAO]):
                    self.lista_distribuicao.append(origem)
    
    
    def haNovosArquivos(self):
        return self.lista_pagamento or self.lista_distribuicao
    
    def processarArquivos(self):
        if self.lista_pagamento:
            for arquivo in self.lista_pagamento:               
                try:
                    if CTLPagamento.salvar(arquivo):    
                        if not self.arquivosCarregados:
                            ut.moverArquivo(self.pasta, self.processados, arquivo)
                        self.gravarArquivoExcelProcessado(arquivo, enTipo.EnumTipoArquivoExcel.PAGAMENTO)
                except Exception as e:
                    e.add_note(f"Falha no processamento de Pagamento {arquivo} -> {e}")
                    self.gravarArquivoExcelProcessado(arquivo, enTipo.EnumTipoArquivoExcel.PAGAMENTO, str(e))
                    raise
        
        if self.lista_distribuicao:            
            for arquivo in self.lista_distribuicao:
                try:
                    if CTLDistribuicao.salvar(arquivo):
                        if not self.arquivosCarregados:
                            ut.moverArquivo(self.pasta, self.processados, arquivo)
                        self.gravarArquivoExcelProcessado(arquivo, enTipo.EnumTipoArquivoExcel.DISTRIBUICAO)
                except Exception as e:
                        e.add_note(f"Falha no processamento de Distribuicao {arquivo} -> {e}")
                        self.gravarArquivoExcelProcessado(arquivo, enTipo.EnumTipoArquivoExcel.DISTRIBUICAO, str(e))
                        raise
    
    def listarArquivosCarregados(self, listaArquivos):
        self.lista_pagamento.clear()
        self.lista_distribuicao.clear()
        self.arquivosExcelImportados.clear()
        if not os.path.isdir(self.processados):
            os.makedirs(self.processados)

        for arquivo in listaArquivos:
            if enTipo.EnumTipoArquivoExcel.PAGAMENTO in arquivo.name.lower():
                self.lista_pagamento.append(arquivo)            
            elif enTipo.EnumTipoArquivoExcel.DISTRIBUICAO in arquivo.name.lower():
                self.lista_distribuicao.append(arquivo)
    
    def gravarArquivoExcelProcessado(self, arquivo, tipo: enTipo.EnumTipoArquivoExcel, resultado: str = 'Processado com sucesso'):
        nome = str(arquivo) if isinstance(arquivo, str) else arquivo.name
        logUpload = entUpl.LogUpload(Nome=nome, Tipo=tipo, Resultado=resultado, Processamento=ut.obterDataHorarioCompleta())
        self.arquivosExcelImportados.append(logUpload)
        CTLLogUpload.salvar(logUpload)
        
        
    def criarDfArquivosExcelImportados(self, arquivosExcelImportados: list) -> pd.DataFrame:
        return pd.DataFrame(arquivosExcelImportados, columns=["Nome", "Tipo", "Resultado"], dtype=entArq.ArquivoExcel)
    
    def criarDfArquivosExcelImportados(self) -> pd.DataFrame:
        return pd.DataFrame(self.arquivosExcelImportados, columns=["Nome", "Tipo", "Resultado"], dtype=entArq.ArquivoExcel)