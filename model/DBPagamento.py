from dataclasses import dataclass
import mysql.connector as my
from model import DbMysql as db
import pandas as pd
from entity import Contratante as entCont

@dataclass
class DBPagamento(db.DbMysql):
    def salvar(self, df) -> bool:
        
        try:
            contratante = df["PagContratante"].unique()
            ano = df["PagAno"].unique()
            mes = df["PagMes"].unique()
            c = tuple(contratante)
            a = tuple(ano)
            m = tuple(mes)
            params = {'c':c, 'a':a, 'm':m}
            
            conn = self.connect()
            cursor = conn.cursor()
            sql_insert = """
                INSERT INTO TbPagamentoBkp 
                SELECT 
                       PagAno,
	                   PagMes,
                       PagContratante, 
                       PagCpfCnpj, 
                       PagNomeCliente, 
                       PagParcelaDataCalculo, 
                       PagTipoNegociacao, 
                       PagVendaQuadraLote, 
                       PagDataAcordo, 
                       PagNumeroAcordo, 
                       PagValorHonorarioAcordo, 
                       PagValorTotalAcordo, 
                       PagVencimentoParcela, 
                       PagDataPagamentoParcela, 
                       PagNossoNumero, 
                       PagNomeCobrador, 
                       PagStatus, 
                       PagEmpreendimento, 
                       PagValorParcela, 
                       PagValorRecuperado, 
                       PagArquivoProcessado
                FROM tbpagamento
                WHERE PagContratante = %s
                and PagAno = %s
                and PagMes = %s
            """
            
            #cursor.execute(sql_insert, (contratante, ano_mes,ano, mes,))
            cursor.execute(sql_insert, (contratante[0], int(ano[0]), int(mes[0]), ))
            sql_delete = """
                DELETE FROM TbPagamento
                WHERE PagContratante = %s
                and PagAno = %s
                and PagMes = %s
            """
           
            cursor.execute(sql_delete, (contratante[0], int(ano[0]), int(mes[0]), ))
            
            conn.commit()
               
            return self.importarDf(df,'tbpagamento','DBPagamento->importar')               
                        
        except KeyError as e:
            print(f'DBPagamento->importar :{str(e.message)}')
            return False
        except my.Error as err:
            print(f'DBPagamento->importar :{str(err)}')
            return False
        except Exception as e:
            print(f'DBPagamento->importar :{str(e)}')
            conn.rollback()
            return False
        finally:
            if conn :
                conn.close()
            
        
        
    def consultarLoteamentoValorPago(self, contratante: entCont.Contratante) -> pd.DataFrame:
        try:
            conn = self.connect()
            cursor = conn.cursor()
                      
            sql = """
                select
                    PagEmpreendimento as Loteamento,
                    sum(PagValorParcela) as Total
                from tbPagamento 
                where PagContratante = %s
                and PagAno = %s
                and PagMes = %s
                group by PagEmpreendimento
                order by 1
            """
            cursor.execute(sql, (contratante.nome, int(contratante.ano), int(contratante.mes),))
            results = cursor.fetchall()
            return self.exportDataFrame(cursor, results)
        finally:
            if conn :
                conn.close()
            
    def consultarLoteamentoValorRecuperado(self, contratante: entCont.Contratante) -> pd.DataFrame:
        try:
            conn = self.connect()
            cursor = conn.cursor()
                      
            sql = """
                select
                    PagEmpreendimento as Loteamento,
                    sum(PagValorRecuperado) as Total
                from tbPagamento 
                where PagContratante = %s
                and PagAno = %s
                and PagMes = %s
                group by PagEmpreendimento
                order by 1
            """
            cursor.execute(sql, (contratante.nome, int(contratante.ano), int(contratante.mes),))
            results = cursor.fetchall()
            return self.exportDataFrame(cursor, results)
        finally:
            if conn :
                conn.close()
            

    def consultarTipoNegociacao(self, contratante: entCont.Contratante) -> pd.DataFrame:
        try:
            conn = self.connect()
            cursor = conn.cursor()
                      
            sql = """
                select
                    PagTipoNegociacao as Tipo,
                    count(PagTipoNegociacao) as Qtde,
                    sum(PagValorRecuperado) as Total
                from tbPagamento 
                where PagContratante = %s
                and PagAno = %s
                and PagMes = %s
                and PagTipoNegociacao is not null
                group by PagTipoNegociacao
                order by 1
            """
            cursor.execute(sql, (contratante.nome, int(contratante.ano), int(contratante.mes),))
            results = cursor.fetchall()
            return self.exportDataFrame(cursor, results)
        finally:
            if conn :
                conn.close()
            

    def consultarContratanteDistinto(self)-> pd.DataFrame:
        try:
            conn = self.connect()
            cursor = conn.cursor()
                      
            sql = """
                select
                    distinct PagContratante as Contratante
                from tbPagamento 
                order by 1
            """
            cursor.execute(sql)
            results = cursor.fetchall()
            return self.exportDataFrame(cursor, results)
        finally:
            if conn :
                conn.close()
            
        
                        
    def consultarContratante(self, nome):
        try:
            conn = self.connect()
            cursor = conn.cursor()
                      
            sql = """
                select *
                from tbPagamento 
                where PagContratante = %s
                order by 1
            """
            cursor.execute(sql, (nome, ))
            results = cursor.fetchall()
            return self.exportDataFrame(cursor, results)
        finally:
            if conn :
                conn.close()
   
            
