from graficos import *

st.title('Execução orçamentário do estado de São Paulo')

st.divider()
st.write('1º Modalidades das despesas realizadas pelo estado de São Paulo.')
primeiroGrafico()

st.divider()
st.write('2º Fontes conhecidas recorridas para os pagamentos realizados no período selecionado.')
segundoGrafico()

st.divider()
st.write("3º Quantidade de reais que foram empenhados, gastos, liquidados ou que foram disponibilizados.")
filtro3 = filtroDespesa()
terceiroGrafico(filtro3)

st.divider()
st.write("4º Proporção entre os tipos de despesas")
filtro4 = filtroAnos()
quartoGrafico(filtro4)