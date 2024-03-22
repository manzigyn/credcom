from dataclasses import dataclass
import mysql.connector as my
from model import DbMysql as db


@dataclass
class DBParametrizacao(db.DbMysql):
    pass