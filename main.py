from graficos import *
from functions import *

st.title('Execução orçamentário do estado de São Paulo')
st.divider()

despesas = filtroDespesa()
anos = filtroAnos()

st.divider()
st.write('1º Modalidade(s) da(s) despesa(s) realizada(s) pelo estado de São Paulo.')
primeiroGrafico(anos, despesas)

st.divider()
st.write('2º Fonte(s) recorridas para os pagamentos realizados no período selecionado.')
segundoGrafico(anos, despesas)

st.divider()
st.write("3º Quantidade de reais empenhados, gastos, liquidados ou que estavam disponíveis.")
terceiroGrafico(despesas)

st.divider()
st.write("4º Proporção entre os tipos de despesas.")
quartoGrafico(anos, despesas)