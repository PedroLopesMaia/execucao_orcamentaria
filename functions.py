import mysql.connector
import streamlit as st
import pandas as pd

from queries import *

def getConexao():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ML$KL9wsJw",
        database="dw_execucao"
    )
    return connection

def createNameColumn(df):
    nome = [df.columns[0] for i in range(len(df.index))]
    df['Nome'] = nome
    return df
def filtroAnos():
    anos = getResposta(query_anos).iloc[1:]
    options = st.multiselect(
        'Ano de exercício:', anos)
    return options

def filtroDespesa():
    despesas = getResposta(query_despesas).iloc[1:]
    filtro = despesas.copy()
    filtro['nome'] = filtro['nome'].apply(lambda x: fix_encoding(x))
    options = st.multiselect(
        'Nome da despesa:', filtro)
    return unfix_encoding(despesas, filtro, options)

def fix_encoding(string):
    return string.encode('cp1252').decode('utf8')

def unfix_encoding(resposta, filtro, options):
    dic_resposta = resposta.to_dict()
    dic_filtro = filtro.to_dict()['nome']
    filtro_dic = {}
    for i in range(len(dic_filtro)):
        filtro_dic[dic_filtro[i+1]] = i+1
    return [dic_resposta['nome'][filtro_dic[string]] for string in options]


def atualizaDataframeDoisFiltros(query, query_filtro, lista_anos, Lista_despesas, token_ano, token_despesa, propriedades,
                                subset_remoção):
    dfs = []
    for ano in lista_anos:
        query_filter = query_filtro.replace(token_ano, str(ano))
        dfs.append(atualizaDataframeUmFiltro(query, query_filter, Lista_despesas, token_despesa, propriedades, subset_remoção))
    return somaDfs(dfs, propriedades, subset_remoção)

def atualizaDataframeUmFiltro(query, query_filter, lista, token, propriedades, subset_remoção):
    df = getResposta(query)
    for i in propriedades:
        df[i].values[:] = 0
    dataframes = [df]
    if len(lista) != 0:
        for placeholder in lista:
            query = query_filter.replace(token, str(placeholder))
            dataframes.append(getResposta(query))
        resposta = somaDfs(dataframes, propriedades, subset_remoção)
    else:
        resposta = getResposta(query)
    return resposta

def somaDfs(dataframes, propriedades, subset_remoção):
    for i in range(len(dataframes)):
        if i == 0:
            resposta = dataframes[0]
        else:
            for propriedade in propriedades:
                temp = resposta.copy()
                temp[propriedade] = resposta[propriedade] + dataframes[i][propriedade]
                temp = temp.dropna()
                resposta = pd.concat([resposta, temp], axis=0)
                resposta = resposta.drop_duplicates(subset=[subset_remoção], keep='last')
    return resposta

def removeVirgula(x):
    x = str(x).replace(',', '')
    return x

def getResposta(query):
    conexao = getConexao()
    df = pd.read_sql(query, conexao)
    return df
