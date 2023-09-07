from graficos import *
from functions import *

st.title('Execução orçamentário do estado de São Paulo')
st.divider()

despesas = filtroDespesa()
anos = filtroAnos()

st.divider()
st.write("Valor total em reais que foram empenhados, gastos, liquidados ou que estavam disponíveis.")
terceiroGrafico(despesas)

st.divider()
st.write('Modalidade(s) da(s) despesa(s) realizada(s) pelo estado de São Paulo.')
primeiroGrafico(anos, despesas)

st.divider()
st.write("Proporção entre os tipos de despesas.")
quartoGrafico(anos, despesas)

st.divider()
st.write("Vinte maiores despesas em quantidade")
quintoGrafico(anos, despesas)

st.divider()
st.write('Fonte(s) recorridas para os pagamentos realizados no período selecionado.')
segundoGrafico(anos, despesas)
