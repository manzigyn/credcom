from dataclasses import dataclass
import mysql.connector as my
from classes import database as db


@dataclass
class DBConfiguracaoResultado(db.DbMysql):
    def consultar(self, contratante, ano, mes):
        try:
            conn = self.connect()
            cursor = conn.cursor()
                      
            sql = """
                SELECT * FROM TBConfiguracaoResultado
                WHERE ConfContratante = %s
                and ConfAno = %s
                and ConfMes = %s
            """
            cursor.execute(sql, (contratante, int(ano), int(mes),))
            results = cursor.fetchall()
            return  self.exportDataFrame(cursor, results)
        finally:
            if conn:
                conn.close()
            
            
    def consultarPadrao(self):
        return self.consultar('padrao',-1,-1)
            
    def importar(self, df):
        try:            
            contratante = df["ConfContratante"].unique()
            ano = df["ConfAno"].unique()
            mes = df["ConfMes"].unique()
            chaves = df["ConfChave"].unique()
            
            conn = self.connect()
            cursor = conn.cursor()
            for chave in chaves:                      
                sql_delete = """
                    DELETE FROM TBConfiguracaoResultado
                    WHERE ConfContratante = %s
                    and ConfAno = %s
                    and ConfMes = %s
                    and ConfChave = %s
                """
                cursor.execute(sql_delete, (contratante[0], int(ano[0]), int(mes[0]),chave, ))
                
            conn.commit()                        
            return self.importarDf(df, 'tbconfiguracaoresultado','DBConfiguracaoResultado->importar')
            
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
                
    
                