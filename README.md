# UFRPE-BSI 2022.2 | Modelagem de Dados

## Grupo 10 - Pedro Lopes

O repositório abriga o código do aplicativo desenvolvido para a disciplina de Modelagem de dados do curso de graduação de Sistemas de Informação da UFRPE.

## Dependências do Projeto

Para instalar as depedências necessárias para o funcionamento do aplicativo, basta executar o comando:

    pip install -r requirements.txt

No arquivo "requirements.txt" estão listadas as bibliotecas/módulos utilizados e suas versões. O data warehouse foi construído com o sistema de gerenciamento MySQL, e para que a leitura dos dados possa ser feita pela aplicação, é preciso que o arquivo presente na pasta "DW" seja importado nesse sistema.

## Variáveis de Ambiente

Para executar o projeto localmente é necessário acessar o arquivo "functions.py", e substitutir as seguintes variáveis presentes na função "getConexao()"":

    def getConexao():
        connection = mysql.connector.connect(
            host=...,
            user=...,
            password=...,
            database=...
        )
        return connection

## Execução do Projeto (Local)

Também é necessário executar o comando a baixo no terminal, na pasta do projeto:

    streamlit run main.py

## Execução do Projeto (Remoto)

O aplicativo pode ser acessado pelo link:

    https://f699-186-231-241-126.ngrok-free.app/