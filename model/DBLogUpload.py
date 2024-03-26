from dataclasses import dataclass
import mysql.connector as my
from model import DbMysql as db
import pandas as pd

@dataclass
class DBLogUpload(db.DbMysql):
    def salvar(self, df) -> bool:
        
        try:            
               
            return self.importarDf(df,'tblogupload','DBLogUpload->importar')               
                        
        except KeyError as e:
            print(f'DBLogUpload->importar :{str(e.message)}')
            return False
        except my.Error as err:
            print(f'DBLogUpload->importar :{str(err)}')
            return False
        except Exception as e:
            print(f'DBLogUpload->importar :{str(e)}')
            return False

    def consultar(self)-> pd.DataFrame:
        try:
            conn = self.connect()
            cursor = conn.cursor()
                      
            sql = """
                select
                    UplNome as Nome,
                    UplTipo as Tipo,
                    UplOperador as Operador,
                    UplResultado as Resultado,
                    UplProcessamento as Processamento
                from TbLogUpload
                order by Processamento desc
            """
            cursor.execute(sql)
            results = cursor.fetchall()
            return self.exportDataFrame(cursor, results)
        finally:
            if conn :
                conn.close()
                
    