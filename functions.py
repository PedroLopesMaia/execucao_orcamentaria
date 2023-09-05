import mysql.connector
import streamlit as st
import pandas as pd

def getConexao():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ML$KL9wsJw",
        database="dw_execucao"
    )
    return connection

def atualizaDataframe(query, query_filter, lista, token, propriedades):
    dataframes = []
    if len(lista) != 0:
        for ano in lista:
            query = query_filter.replace(token, str(ano))
            dataframes.append(getResposta(query))
        for i in range(len(dataframes)):
            if i == 0:
                resposta = dataframes[0]
            else:
                for propriedade in propriedades:
                    resposta[propriedade] = resposta[propriedade] + dataframes[i][propriedade]
    else:
        resposta = getResposta(query)
    return resposta

def removeVirgula(x):
    x = str(x).replace(',', '')
    return x

def getResposta(query):
    conexao = getConexao()
    df = pd.read_sql(query, conexao)
    return df
