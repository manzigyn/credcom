from dataclasses import dataclass
import mysql.connector as my
from model import DbMysql as db
import pandas as pd
from entity import Contratante as entCont


@dataclass
class DBLogGeracao(db.DbMysql):
    def salvar(self, df) -> bool:
        
        try:            
               
            return self.importarDf(df,'tbloggeracao','DBLogGeracao->importar')               
                        
        except KeyError as e:
            print(f'DBLogGeracao->importar :{str(e.message)}')
            return False
        except my.Error as err:
            print(f'DBLogGeracao->importar :{str(err)}')
            return False
        except Exception as e:
            print(f'DBLogGeracao->importar :{str(e)}')
            return False

    def consultarAnoMesDistinto(self)-> pd.DataFrame:
        try:
            conn = self.connect()
            cursor = conn.cursor()
                      
            sql = """
                select
                    distinct 
                             GerAno as Ano,
                             GerMes as Mes
                from tbLogGeracao
                order by Ano desc, Mes
            """
            cursor.execute(sql)
            results = cursor.fetchall()
            return self.exportDataFrame(cursor, results)
        finally:
            if conn :
                conn.close()
                
    def consultar(self)-> pd.DataFrame:
        try:
            conn = self.connect()
            cursor = conn.cursor()
                                     
            sql = """
                select distinct 
                        p.PagContratante as Contratante,
                        p.PagAno  as Ano,
                        p.PagMes as Mes,
                        l.GerOperador as Operador,
                        l.GerData as Data,
                        l.GerHorario as Horario,
                        l.GerArquivo as Arquivo,
                        l.GerCaminho as Caminho
                    from tbpagamento p
                    left join tbloggeracao l on l.GerContratante = p.PagContratante and l.GerAno = p.PagAno and l.GerMes = p.PagMes
                    order by Ano desc, Mes desc, Contratante, Data desc, Horario desc 
            """
            cursor.execute(sql)
            results = cursor.fetchall()
            return self.exportDataFrame(cursor, results)
        finally:
            if conn :
                conn.close()                