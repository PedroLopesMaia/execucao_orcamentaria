import streamlit as st
import os
import mysql.connector
import pandas as pd
import plotly.express as px


def estabelecer_conexao_bd():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ML$KL9wsJw",
        database="dw_execucao"
    )
    return connection


conexao = estabelecer_conexao_bd()

query = "SELECT * FROM dm_tempo;"

df = pd.read_sql(query, conexao)

df
