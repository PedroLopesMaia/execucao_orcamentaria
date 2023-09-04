import mysql.connector
import pandas as pd

def getConexao():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ML$KL9wsJw",
        database="dw_execucao"
    )
    return connection

def removeVirgula(x):
    x = str(x).replace(',', '')
    return x

def getResposta(query):
    conexao = getConexao()
    df = pd.read_sql(query, conexao)
    return df