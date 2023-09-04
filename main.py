from graficos import *

st.title('Execução orçamentário do estado de São Paulo')

st.divider()
st.write('1º As 8 fontes mais frenquentes nas execuções orçamentárias durante o ano selecionados?')
primeiroGrafico()

st.write('2º Com qual frequência o estado de São Paulo gastou com "aposentadorias e reformas", "Pensões", "Auxílio alimentação" e "Material de consumo"?')

st.divider()
st.write("3º Quantidade de reais que foram empenhados, gastos, liquidados e que foram disponíveis para despesas relativas a gastos com municípios até 2015.")
terceiroGrafico()

st.divider()
st.write("4º Qual é a proporção entre os tipos de despesas?")
quartoGrafico()