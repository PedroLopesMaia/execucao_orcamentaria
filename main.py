from graficos import *

st.title('Execução orçamentário do estado de São Paulo')

st.divider()
st.write('1º As 7 maiores modalidades de despesas do estado de São Paulo.')
primeiroGrafico()

st.divider()
st.write('2º Transferências de fontes conhecidas realizadas no período selecionado.')
segundoGrafico()

st.divider()
st.write("3º Quantidade de reais que foram empenhados, gastos, liquidados ou que foram disponibilizados.")
terceiroGrafico()

st.divider()
st.write("4º Proporção entre os tipos de despesas")
quartoGrafico()