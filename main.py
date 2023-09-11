from graficos import *
from functions import *

st.title('Execução orçamentário do estado de São Paulo')
st.divider()

despesas = filtroDespesa()
anos = filtroAnos()

st.divider()
st.subheader("Valor total em reais que foram empenhados, gastos, liquidados ou que estavam disponíveis.")
terceiroGrafico(despesas)
st.write('Gráfico utilizado para responder a pergunta 3.')

st.divider()
st.subheader('Modalidade(s) da(s) despesa(s) realizada(s) pelo estado de São Paulo.')
primeiroGrafico(anos, despesas)
st.write('Gráfico utilizado para responder a pergunta 5.')

st.divider()
st.subheader("Proporção entre os tipos de despesas.")
quartoGrafico(anos, despesas)
st.write('Gráfico utilizado para responder a pergunta 2.')

st.divider()
st.subheader("Vinte maiores despesas em quantidade")
quintoGrafico(anos, despesas)
st.write('Gráfico utilizado para responder a pergunta 4.')

st.divider()
st.subheader('Fonte(s) recorridas para os pagamentos realizados no período selecionado.')
segundoGrafico(anos, despesas)
st.write('Gráfico utilizado para responder a pergunta 1.')
