import streamlit as st
import altair as alt
import plotly.express as px
import pandas as pd

from functions import removeVirgula, getResposta

query1 = "SELECT COUNT(nome) AS Frequência, nome AS Nome from dm_modalidade INNER JOIN ft_pagamento on modalidadekey = " \
         "dm_modalidade.key GROUP BY nome;"
query4 = "SELECT COUNT(nome) AS quantidade, nome AS categoria from dm_categoria_despesa INNER JOIN ft_pagamento on " \
         "categoria_despesakey = dm_categoria_despesa.key " \
         "GROUP BY nome ORDER BY quantidade DESC;"
query2 = "SELECT COUNT(nome) AS Frequência, nome AS Fonte from dm_fonte INNER JOIN ft_pagamento on fontekey = dm_fonte.key" \
         " GROUP BY nome ORDER BY Frequência DESC;"
query3 = "SELECT Vl_Pago AS Pago, Vl_EmpenhadoLiquido AS Empenhado, Vl_Liquidado AS Liquidado, Disponivel, AnoExercicio" \
         " AS Ano from ft_pagamento INNER JOIN dm_tempo on ft_pagamento.tempokey = dm_tempo.key GROUP BY Ano; "

def primeiroGrafico():
    resposta1 = getResposta(query1)
    linhas_selecionadas = resposta1.copy().iloc[:7]

    st.bar_chart(
        linhas_selecionadas,
        x='Nome',
        y='Frequência',
        width=400,
        height=600
    )

def segundoGrafico():
    resposta2 = getResposta(query2)
    resposta2 = resposta2.iloc[1:]
    # trans_federal = resposta2['Frequência'][0]
    # trans_estadual = resposta2['Frequência'][1]
    # df = pd.DataFrame([[trans_federal, trans_estadual]], columns=['Federal', 'Estadual'])
    c = alt.Chart(resposta2).mark_circle().encode(
        x='Frequência', y='Fonte', size='Frequência', color='Frequência', tooltip=['Frequência','Fonte'])

    st.altair_chart(c, use_container_width=True)


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
    categoria = ["Despesas de Capital", "Despesas Correntes", "Reserva Contigencia"]
    cores = ["#aa423a", "#f6b404", "#327a88"]
    categoria_select = alt.selection_single(fields=["categoria"], empty="all")
    categoria_pie = (
        (
            alt.Chart(resposta4)
            .mark_arc(innerRadius=50)
            .encode(
                theta=alt.Theta(
                    "quantidade",
                    type="quantitative",
                    aggregate="sum",
                    title="Quantidade",
                ),
                color=alt.Color(
                    field="categoria",
                    type="nominal",
                    scale=alt.Scale(domain=categoria, range=cores),
                    title="Categoria",
                ),
                opacity=alt.condition(categoria_select, alt.value(1), alt.value(0.25)),
            )
        )
        .add_selection(categoria_select)
    )
    st.altair_chart(categoria_pie)