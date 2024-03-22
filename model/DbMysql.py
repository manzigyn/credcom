from dataclasses import dataclass
import mysql.connector as my
from sqlalchemy import create_engine
import pandas as pd

@dataclass
class DbMysql:
    myUser: str = "credcom"
    myPwd: str = "credcom"
    myDb: str = "credcom"
    myHost: str = "localhost"
    
    def connect(self):
        conn = my.connect(user = self.myUser,
            password = self.myPwd,
            host = self.myHost,
            database = self.myDb)   
        return conn
    
    def connect_engine(self):
        db_url = "mysql+mysqlconnector://{USER}:{PWD}@{HOST}:{PORT}/{DBNAME}"
        db_url = db_url.format(
            USER = self.myUser,
            PWD = self.myPwd,
            HOST = f"{self.myHost}",
            DBNAME = self.myDb,
            PORT = 3306
        )   
        return create_engine(db_url, echo=False)
    
    
    def query(self, sql_query):
        with self.connect().cursor() as cursor:
            cursor.execute(sql_query)
            return cursor.fetchall()

    def query(self, sql_query, params):
        with self.connect().cursor() as cursor:
            cursor.execute(sql_query,params)        
            return cursor.fetchall()

    def execute(self, sql_dml):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(sql_dml)
            conn.commit()
        finally:
            conn.close()

    def execute(self, sql_dml, params):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(sql_dml, params)
            conn.commit()
        finally:
            conn.close()
            
    def exportDataFrame(self, cursor, rows) -> pd.DataFrame:
        names = [ x[0] for x in cursor.description]
        return pd.DataFrame(rows, columns=names)
    
    def importarDf(self, df, table, messageError) -> bool:
        try:
            dbEngine = self.connect_engine()
            #with dbEngine.begin() as conn2:
            df.to_sql(
                    name=table, 
                    con=dbEngine, 
                    index=False, 
                    if_exists='append'
                )
            return True
        except Exception as e:
            print(f'{messageError} :{str(e)}')
            return False      