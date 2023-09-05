from graficos import *
from functions import *

st.title('Execução orçamentário do estado de São Paulo')
st.divider()

despesas = filtroDespesa()
anos = filtroAnos()

st.divider()
st.write('1º Modalidades das despesas realizadas pelo estado de São Paulo.')
primeiroGrafico(anos, despesas)

st.divider()
st.write('2º Fontes conhecidas recorridas para os pagamentos realizados no período selecionado.')
segundoGrafico(anos, despesas)

st.divider()
st.write("3º Quantidade de reais que foram empenhados, gastos, liquidados ou que foram disponibilizados.")
terceiroGrafico(despesas)

st.divider()
st.write("4º Proporção entre os tipos de despesas")
quartoGrafico(anos, despesas)