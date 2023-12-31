import altair as alt

from functions import *
from queries import *

def primeiroGrafico(anos, despesas):
    if len(anos) != 0 and len(despesas) != 0:
        resposta = atualizaDataframeDoisFiltros(query1, query1_filter, anos, despesas, '{AnoExercicio}', '{despesa}', ['Frequência'], 'Modalidade')
    elif len(anos) != 0 and len(despesas) == 0:
        resposta = atualizaDataframeUmFiltro(query1, query1_filter_ano, anos, '{AnoExercicio}', ['Frequência'], 'Modalidade')
    elif len(anos) == 0 and len(despesas) != 0:
        resposta = atualizaDataframeUmFiltro(query1, query1_filter_despesa, despesas, '{despesa}', ['Frequência'], 'Modalidade')
    else:
        resposta = getResposta(query1)
    resposta['Modalidade'] = resposta['Modalidade'].apply(lambda x : fix_encoding(x))

    st.bar_chart(
        resposta,
        x='Modalidade',
        y='Frequência',
        width=400,
        height=600,
    )

def quintoGrafico(anos, despesas):
    if len(anos) != 0 and len(despesas) == 0:
        resposta = atualizaDataframeUmFiltro(query5, query5_filter_ano, anos, '{AnoExercicio}', ['Quantidade'],
                                             'Despesa')
        resposta= resposta[resposta['Quantidade'] != 0]
    else:
        resposta = getResposta(query5)
    resposta['Despesa'] = resposta['Despesa'].apply(lambda x: fix_encoding(x))
    c = alt.Chart(resposta.iloc[:20]).mark_circle().encode(
        x='Quantidade', y='Despesa', size='Quantidade', color='Quantidade', tooltip=['Quantidade','Despesa'])
    st.altair_chart(c, use_container_width=True)


def segundoGrafico(anos, despesas):
    if len(anos) != 0 and len(despesas) != 0:
        resposta = atualizaDataframeDoisFiltros(query2, query2_filter, anos, despesas, '{AnoExercicio}', '{despesa}', ['Valor'], 'Fonte')
    elif len(anos) != 0 and len(despesas) == 0:
        resposta = atualizaDataframeUmFiltro(query2, query2_filter_ano, anos, '{AnoExercicio}', ['Valor'], 'Fonte')
    elif len(anos) == 0 and len(despesas) != 0:
        resposta = atualizaDataframeUmFiltro(query2, query2_filter_despesa, despesas, '{despesa}', ['Valor'], 'Fonte')
    else:
        resposta = getResposta(query2)
    resposta = resposta.iloc[1:]
    resposta['Fonte'] = resposta['Fonte'].apply(lambda x: fix_encoding(x))
    st.bar_chart(
        resposta,
        x='Fonte',
        y='Valor',
        width=400,
        height=600,
    )
    # c = alt.Chart(resposta).mark_circle().encode(
    #     x='Frequência', y='Fonte', size='Frequência', color='Frequência', tooltip=['Frequência','Fonte'])
    # st.altair_chart(c, use_container_width=True)


def terceiroGrafico(despesas):
    if len(despesas) != 0:
        resposta = atualizaDataframeUmFiltro(query3, query3_filter_despesa, despesas, '{despesa}', ['Pago', 'Empenhado', 'Liquidado', 'Disponivel'], 'Ano')
    else:
        resposta = getResposta(query3)
    resposta['Ano'] = resposta['Ano'].apply(removeVirgula)
    st.line_chart(
        resposta.iloc[2:],
        y=['Pago', 'Empenhado', 'Liquidado', 'Disponivel'],
        x='Ano'
    )

def quartoGrafico(anos, despesas):
    if len(anos) != 0 and len(despesas) != 0:
        resposta = atualizaDataframeDoisFiltros(query4, query4_filter, anos, despesas, '{AnoExercicio}', '{despesa}', ['quantidade'], 'categoria')
    elif len(anos) != 0 and len(despesas) == 0:
        resposta = atualizaDataframeUmFiltro(query4, query4_filter_ano, anos, '{AnoExercicio}', ['quantidade'], 'categoria')
    elif len(anos) == 0 and len(despesas) != 0:
        resposta = atualizaDataframeUmFiltro(query4, query4_filter_despesa, despesas, '{despesa}', ['quantidade'], 'categoria')
    else:
        resposta = getResposta(query4)
    categoria = ["Despesas de Capital", "Despesas Correntes", "Reserva Contigencial"]
    cores = ["#aa423a", "#f6b404", "#327a88"]
    categoria_select = alt.selection_single(fields=["categoria"], empty="all")
    categoria_pie = (
        (
            alt.Chart(resposta)
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