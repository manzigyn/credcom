from dataclasses import dataclass
import mysql.connector as my
from model import DbMysql as db
import pandas as pd

@dataclass
class DBParametrizacao(db.DbMysql):
    def consultar(self, chave) -> pd.DataFrame:
        try:
            conn = self.connect()
            cursor = conn.cursor()
                      
            sql = """
                SELECT * FROM TBParametrizacao
                WHERE ParChave = %s
            """
            cursor.execute(sql, (str(chave).lower,))
            results = cursor.fetchall()
            return  self.exportDataFrame(cursor, results)
        finally:
            if conn:
                conn.close()
                
    def consultarTodos(self) -> pd.DataFrame:
        try:
            conn = self.connect()
            cursor = conn.cursor()
                      
            sql = """
                SELECT * FROM TBParametrizacao
            """
            cursor.execute(sql)
            results = cursor.fetchall()
            return  self.exportDataFrame(cursor, results)
        finally:
            if conn:
                conn.close()    
                
    def salvar(self, df) -> bool:
        try:            
            chaves = df["ParChave"].unique()
            
            conn = self.connect()
            cursor = conn.cursor()
            for chave in chaves:                      
                sql_delete = """
                    DELETE FROM TBParametrizacao
                    WHERE ParChave = %s
                """
                cursor.execute(sql_delete, (chave, ))
                
            conn.commit()                        
            return self.importarDf(df, 'tbparametrizacao','DBParametrizacao->importar')
            
        except KeyError as e:
            print(f'DBParametrizacao->importar :{str(e.message)}')
            return False
        except my.Error as err:
            print(f'DBParametrizacao->importar :{str(err)}')
            return False
        except Exception as e:
            print(f'DBParametrizacao->importar :{str(e)}')
            conn.rollback()
            return False    
        finally:
            if conn:
                conn.close()                             