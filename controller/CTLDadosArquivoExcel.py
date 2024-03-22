from dataclasses import dataclass
import pandas as pd
from utils import utilidades as ut
from controller import CTLPagamento 
from controller import CTLDistribuicao
from controller import CTLParametrizacao 
import os


@dataclass
class DadosArquivoExcel():
    lista_pagamento = []
    lista_distribuicao = []
    parametrizacao = CTLParametrizacao.carregar()
    pasta = parametrizacao.dir_dados if parametrizacao.dir_dados else 'dados/' 
    processados = parametrizacao.dir_processados if parametrizacao.dir_processados else f'dados/processados/'
    
    def __init__(self):
        self.listarArquivos()
    
    def listarArquivos(self):
        self.lista_pagamento.clear()
        self.lista_distribuicao.clear()
        if not os.path.isdir(self.processados):
            os.makedirs(self.processados)

        for arquivo in os.listdir(self.pasta):
            if arquivo.endswith(".xlsx"): 
                origem = f'{self.pasta}{arquivo}'
                if any(x in arquivo for x in ["pagamento"]):
                    self.lista_pagamento.append(origem)            
                elif any(x in arquivo for x in ["distribuicao"]):
                    self.lista_distribuicao.append(origem)
    
    
    def haNovosArquivos(self):
        return self.lista_pagamento or self.lista_distribuicao
    
    def processarArquivos(self):
        if self.lista_pagamento:
            try:
                for arquivo in self.lista_pagamento:               
                        if CTLPagamento.salvar(arquivo):               
                            ut.moverArquivo(self.pasta, self.processados, arquivo)
            except Exception as e:
                e.add_note(f"Falha no processamento de Pagamento {arquivo} -> {e}")
                raise
        
        if self.lista_distribuicao:
            try:
                for arquivo in self.lista_distribuicao:
                    if CTLDistribuicao.salvar(arquivo):
                        ut.moverArquivo(self.pasta, self.processados, arquivo)
            except Exception as e:
                    e.add_note(f"Falha no processamento de Distribuicao {arquivo} -> {e}")
                    raise
