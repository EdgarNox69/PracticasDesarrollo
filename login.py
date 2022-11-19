import pymysql
from datetime import datetime
import os

registro = {}

def conectarse()->None:
    return pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='2117',
                                db='bd_practica')

def incio(usuario:str)->None:
    now = datetime.now()
    registro[usuario] = {"fecha y hora de inicio de sesion": now}