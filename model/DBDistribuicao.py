from dataclasses import dataclass
import mysql.connector as my
from model import DbMysql as db
import pandas as pd
from enums import EnumConfiguracaoResultado as enConfig
from entity import Contratante as entCont

@dataclass
class DBDistribuicao(db.DbMysql):
    def salvar(self, df) -> bool:
        try:
            carteira = df["DisCarteira"].unique()
            
            conn = self.connect()
            cursor = conn.cursor()
            sql_insert = """
                INSERT INTO TbDistribuicaoBkp 
                SELECT 
                       DisCarteira, 
                       DisOperador, 
                       DisNumeroParcelas, 
                       DisVenda, 
                       DisUnidade, 
                       DisCodigoClienteContrato, 
                       DisLoteamentoCursoLuc, 
                       DisAtrasoReal, 
                       DisValorTotal, 
                       DisStatus, 
                       DisCpfCnpj, 
                       DisNome, 
                       DisStatus2, 
                       DisStatusVirtua, 
                       DisArquivoProcessado
                FROM tbdistribuicao
                WHERE DisCarteira = %s
            """
            c = tuple()
            cursor.execute(sql_insert, (carteira[0],))
            sql_delete = """
                DELETE FROM tbdistribuicao
                WHERE DisCarteira = %s
            """
            cursor.execute(sql_delete, (carteira[0], ))
            conn.commit();
            return self.importarDf(df,'tbdistribuicao','DBDistribuicao->importar')
                
        except KeyError as e:
            print(f'DBDistribuicao->importar :{str(e.message)}')
            return False
        except my.Error as err:
            print(f'DBDistribuicao->importar :{str(err)}')
            return False
        except Exception as e:
            print(f'DBDistribuicao->importar :{str(e)}')
            conn.rollback()
            return False    
        finally:
            if conn:
                conn.close()
                
   
            
    def consultarLoteamentoValorTotal(self, contratante: entCont.Contratante) -> pd.DataFrame:
        try:
            conn = self.connect()
            cursor = conn.cursor()
                      
            sql = """
                select d.DisLoteamentoCursoLuc as Loteamento,
                    count(d.DisLoteamentoCursoLuc) as Qtde,
                    sum(d.DisValorTotal) as TotalInadimplencia
                from TbDistribuicao d
                where d.DisLoteamentoCursoLuc is not null
                and  d.DisCarteira = %s
                and exists (
                    select 1 from TBConfiguracaoResultado c 
                    where c.ConfContratante = d.DisCarteira
                    and c.ConfAno = %s
                    and c.ConfMes = %s
                    and c.ConfChave = %s
                    and c.ConfValor = d.DisStatusVirtua
                    )
                group by d.DisLoteamentoCursoLuc
                order by 1
            """
            cursor.execute(sql, (contratante.nome, int(contratante.ano), int(contratante.mes), enConfig.EnumConfiguracaoResultado.STATUS, ))
            results = cursor.fetchall()
            return self.exportDataFrame(cursor, results)
        finally:
            if conn:
                conn.close()
    
            
    def consultarStatusVirtuaTotal(self, nome) -> pd.DataFrame:
        try:
            conn = self.connect()
            cursor = conn.cursor()
                      
            sql = """
                select DisStatusVirtua as Status,
                    count(DisStatusVirtua) as Quantidade
                from TbDistribuicao
                where DisCarteira = %s
                and DisStatusVirtua is not null
                group by DisStatusVirtua
                order by 2 desc
            """
            cursor.execute(sql, (nome,))
            results = cursor.fetchall()
            return self.exportDataFrame(cursor, results)
        finally:
            if conn:
                conn.close()

            
    def consultarContratante(self, nome) -> pd.DataFrame:
        try:
            conn = self.connect()
            cursor = conn.cursor()
                      
            sql = """
                select *
                from TbDistribuicao 
                where DisCarteira = %s
                order by 1
            """
            cursor.execute(sql, (nome, ))
            results = cursor.fetchall()
            return self.exportDataFrame(cursor, results)
        finally:
            if conn:
                conn.close()
                
    def consultarStatusVirtuaDistintos(self, nome) -> pd.DataFrame:
        try:
            conn = self.connect()
            cursor = conn.cursor()
                      
            sql = """
                select  distinct 
                    DisStatusVirtua as StatusVirtua
                from TbDistribuicao 
                where DisCarteira = %s
                order by 1
            """
            cursor.execute(sql, (nome, ))
            results = cursor.fetchall()
            return self.exportDataFrame(cursor, results)
        finally:
            if conn:
                conn.close()                
            
