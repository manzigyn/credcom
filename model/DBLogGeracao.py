from dataclasses import dataclass
import mysql.connector as my
from model import DbMysql as db
import pandas as pd

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
                    distinct GerAno as Ano,
                             GerMes as Mes
                from tbLogGeracao
                order by 1 desc, 2 
            """
            cursor.execute(sql)
            results = cursor.fetchall()
            return self.exportDataFrame(cursor, results)
        finally:
            if conn :
                conn.close()