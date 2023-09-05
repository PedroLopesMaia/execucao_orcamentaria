import altair as alt

from functions import *
from queries import *

def primeiroGrafico():
    resposta1 = getResposta(query1)
    st.bar_chart(
        resposta1,
        x='Nome',
        y='Frequência',
        width=400,
        height=600,
    )

def segundoGrafico():
    resposta2 = getResposta(query2)
    resposta2 = resposta2.iloc[1:]
    c = alt.Chart(resposta2).mark_circle().encode(
        x='Frequência', y='Fonte', size='Frequência', color='Frequência', tooltip=['Frequência','Fonte'])
    st.altair_chart(c, use_container_width=True)


def terceiroGrafico(filtros):
    resposta = atualizaDataframe(query3, query3_filter, filtros, '{despesa}', ['Pago', 'Empenhado', 'Liquidado', 'Disponivel'])
    resposta['Ano'] = resposta['Ano'].apply(removeVirgula)
    st.line_chart(
        resposta,
        y=['Pago', 'Empenhado', 'Liquidado', 'Disponivel'],
        x='Ano'
    )

def filtroAnos():
    anos = getResposta(query_anos).iloc[1:]
    options = st.multiselect(
        'Ano de exercício:', anos)
    return options

def filtroDespesa():
    despesas = getResposta(query_despesas).iloc[1:]
    options = st.multiselect(
        'Nome da despesa:', despesas)
    return options


def quartoGrafico(lista_anos):
    resposta = atualizaDataframe(query4, query4_filter, lista_anos, '{AnoExercicio}', ['quantidade'])

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