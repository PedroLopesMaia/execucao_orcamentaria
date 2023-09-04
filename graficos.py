import streamlit as st
import matplotlib.pyplot as plt

from functions import removeVirgula, getResposta

query1 = "SELECT COUNT(nome) AS Frequência, nome AS Nome from dm_fonte INNER JOIN ft_pagamento on fontekey = dm_fonte.key GROUP BY nome;"
query4 = "SELECT COUNT(nome) AS qtd, nome from dm_categoria_despesa INNER JOIN ft_pagamento on categoria_despesakey = dm_categoria_despesa.key " \
         "GROUP BY nome ORDER BY qtd DESC;"
query3 = "SELECT Vl_Pago AS Pago, Vl_EmpenhadoLiquido AS Empenhado, Vl_Liquidado AS Liquidado, Disponivel, AnoExercicio AS Ano " \
         "from dm_modalidade INNER JOIN ft_pagamento on dm_modalidade.key = modalidadekey" \
         " INNER JOIN dm_tempo on ft_pagamento.tempokey = dm_tempo.key WHERE dm_modalidade.codigo = 40 GROUP BY Ano; "

def primeiroGrafico():
    resposta1 = getResposta(query1)
    linhas_selecionadas = resposta1.copy().iloc[:8]

    st.bar_chart(
        linhas_selecionadas,
        x='Nome',
        y='Frequência',
        width=400,
        height=600
    )


def terceiroGrafico():
    resposta3 = getResposta(query3)
    resposta3['Ano'] = resposta3['Ano'].apply(removeVirgula)
    st.line_chart(
        resposta3,
        y=['Pago', 'Empenhado', 'Liquidado', 'Disponivel'],
        x='Ano'
    )


def quartoGrafico():
    resposta4 = getResposta(query4)
    qtd = resposta4['qtd'].values.tolist()
    explode = (0, 0.1, 0)
    labels = resposta4['nome'].values.tolist()
    fig1, ax1 = plt.subplots()
    ax1.pie(qtd, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)