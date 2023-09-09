# Pesquisa por todas as modalidades de despesas
query1 = "SELECT COUNT(nome) AS Frequência, nome AS Modalidade " \
         "from dm_modalidade " \
         "INNER JOIN ft_pagamento " \
         "on modalidadekey = dm_modalidade.key " \
         "GROUP BY nome;"

# Pesquisa por modalidades de despesas, filtradas por anos de exercício e despesas
query1_filter = "SELECT COUNT(dm_modalidade.nome) AS Frequência, dm_modalidade.nome AS Modalidade " \
                "from dm_modalidade INNER JOIN ft_pagamento " \
                "on modalidadekey = dm_modalidade.key " \
                "INNER JOIN dm_tempo " \
                "on dm_tempo.key = tempokey " \
                "INNER JOIN dm_despesa " \
                "on dm_despesa.key = despesakey " \
                "WHERE AnoExercicio = {AnoExercicio} " \
                "AND dm_despesa.nome = '{despesa}' " \
                "GROUP BY dm_modalidade.nome;"

# Pesquisa por modalidades de despesa, filtradas por anos de exercício
query1_filter_ano = "SELECT COUNT(dm_modalidade.nome) AS Frequência, dm_modalidade.nome AS Modalidade " \
                    "from dm_modalidade INNER JOIN ft_pagamento " \
                    "on modalidadekey = dm_modalidade.key " \
                    "INNER JOIN dm_tempo " \
                    "on dm_tempo.key = tempokey " \
                    "WHERE AnoExercicio = {AnoExercicio} " \
                    "GROUP BY dm_modalidade.nome;"

# Pesquisa por modalidades de despesa, filtradas por despesas
query1_filter_despesa = "SELECT COUNT(dm_modalidade.nome) AS Frequência, dm_modalidade.nome AS Modalidade " \
                        "from dm_modalidade " \
                        "INNER JOIN ft_pagamento " \
                        "on modalidadekey = dm_modalidade.key " \
                        "INNER JOIN dm_despesa " \
                        "on dm_despesa.key = despesakey " \
                        "WHERE dm_despesa.nome = '{despesa}' " \
                        "GROUP BY dm_modalidade.nome;"

# Pesquisa por todas as fontes de recursos
query2 = "SELECT SUM(Vl_pago) AS Valor, nome AS Fonte " \
         "from dm_fonte " \
         "INNER JOIN ft_pagamento " \
         "on fontekey = dm_fonte.key " \
         "GROUP BY nome " \
         "ORDER BY Valor DESC;"

# Pesquisa por fontes de recursos, filtradas por anos de exercício e despesas
# query2_filter = "SELECT COUNT(dm_fonte.nome) AS Frequência, dm_fonte.nome AS Fonte " \
#                 "from dm_fonte " \
#                 "INNER JOIN ft_pagamento " \
#                 "on fontekey = dm_fonte.key " \
#                 "INNER JOIN dm_tempo " \
#                 "on dm_tempo.key = tempokey " \
#                 "INNER JOIN dm_despesa " \
#                 "on dm_despesa.key = despesakey " \
#                 "WHERE AnoExercicio = {AnoExercicio} " \
#                 "AND dm_despesa.nome = '{despesa}' " \
#                 "GROUP BY dm_fonte.nome " \
#                 "ORDER BY Frequência DESC;"

query2_filter = "SELECT SUM(Vl_Pago) AS Valor, dm_fonte.nome AS Fonte " \
                "from dm_fonte " \
                "INNER JOIN ft_pagamento " \
                "on fontekey = dm_fonte.key " \
                "INNER JOIN dm_tempo " \
                "on dm_tempo.key = tempokey " \
                "INNER JOIN dm_despesa " \
                "on dm_despesa.key = despesakey " \
                "WHERE AnoExercicio = {AnoExercicio} " \
                "AND dm_despesa.nome = '{despesa}' " \
                "GROUP BY Fonte " \
                "ORDER BY Valor DESC;"

# Pesquisa por modalidades de despesa, filtradas por anos de exercício
# query2_filter_ano = "SELECT COUNT(dm_fonte.nome) AS Frequência, dm_fonte.nome AS Fonte " \
#                     "from dm_fonte " \
#                     "INNER JOIN ft_pagamento " \
#                     "on fontekey = dm_fonte.key " \
#                     "INNER JOIN dm_tempo " \
#                     "on dm_tempo.key = tempokey " \
#                     "WHERE AnoExercicio = {AnoExercicio} " \
#                     "GROUP BY dm_fonte.nome " \
#                     "ORDER BY Frequência DESC;"

query2_filter_ano = "SELECT SUM(Vl_Pago) AS Valor, dm_fonte.nome AS Fonte " \
                "from dm_fonte " \
                "INNER JOIN ft_pagamento " \
                "on fontekey = dm_fonte.key " \
                "INNER JOIN dm_tempo " \
                "on dm_tempo.key = tempokey " \
                "WHERE AnoExercicio = {AnoExercicio} " \
                "GROUP BY Fonte " \
                "ORDER BY Valor DESC;"

# Pesquisa por modalidades de despesa, filtradas por despesas
# query2_filter_despesa = "SELECT COUNT(dm_fonte.nome) AS Frequência, dm_fonte.nome AS Fonte " \
#                         "from dm_fonte " \
#                         "INNER JOIN ft_pagamento " \
#                         "on fontekey = dm_fonte.key " \
#                         "INNER JOIN dm_despesa " \
#                         "on dm_despesa.key = despesakey " \
#                         "WHERE dm_despesa.nome = '{despesa}' " \
#                         "GROUP BY dm_fonte.nome " \
#                         "ORDER BY Frequência DESC;"

query2_filter_despesa = "SELECT SUM(Vl_Pago) AS Valor, dm_fonte.nome AS Fonte " \
                "from dm_fonte " \
                "INNER JOIN ft_pagamento " \
                "on fontekey = dm_fonte.key " \
                "INNER JOIN dm_despesa " \
                "on dm_despesa.key = despesakey " \
                "AND dm_despesa.nome = '{despesa}' " \
                "GROUP BY Fonte " \
                "ORDER BY Valor DESC;"

# Pesquisa por todos os valores monetários
query3 = "SELECT sum(Vl_Pago) AS Pago, sum(Vl_EmpenhadoLiquido) AS Empenhado, sum(Vl_Liquidado) AS Liquidado, sum(Disponivel) AS Disponivel, AnoExercicio AS Ano " \
         "from ft_pagamento " \
         "INNER JOIN dm_tempo " \
         "on ft_pagamento.tempokey = dm_tempo.key " \
         "GROUP BY Ano; "

# Pesquisa por os valores monetários, filtrados por despesas
query3_filter_despesa = "SELECT sum(Vl_Pago) AS Pago, sum(Vl_EmpenhadoLiquido) AS Empenhado, sum(Vl_Liquidado) AS Liquidado, sum(Disponivel) AS Disponivel, AnoExercicio AS Ano " \
                        "from ft_pagamento " \
                        "INNER JOIN dm_tempo " \
                        "on tempokey = dm_tempo.key " \
                        "INNER JOIN dm_despesa " \
                        "on despesakey = dm_despesa.key " \
                        "WHERE nome = '{despesa}' " \
                        "GROUP BY Ano;"

# Pesquisa por todas as categorias de despesas
query4 = "SELECT COUNT(nome) AS quantidade, nome AS categoria " \
         "from dm_categoria_despesa " \
         "INNER JOIN ft_pagamento " \
         "on categoria_despesakey = dm_categoria_despesa.key " \
         "GROUP BY nome " \
         "ORDER BY quantidade DESC;"

# Pesquisa por categorias de despesas, filtradas por anos de exercício e despesas
query4_filter = "SELECT COUNT(dm_categoria_despesa.nome) AS quantidade, dm_categoria_despesa.nome AS categoria " \
                "from dm_categoria_despesa " \
                "INNER JOIN ft_pagamento " \
                "on categoria_despesakey = dm_categoria_despesa.key " \
                "INNER JOIN dm_despesa " \
                "on dm_despesa.key = despesakey " \
                "INNER JOIN dm_tempo " \
                "on dm_tempo.key = tempokey " \
                "WHERE AnoExercicio = {AnoExercicio} " \
                "AND dm_despesa.nome = '{despesa}' " \
                "GROUP BY dm_categoria_despesa.nome " \
                "ORDER BY dm_categoria_despesa.nome DESC;"

# Pesquisa por categorias de despesas, filtradas por anos de exercício
query4_filter_ano = "SELECT COUNT(nome) AS quantidade, nome AS categoria " \
                    "from dm_categoria_despesa " \
                    "INNER JOIN ft_pagamento " \
                    "on categoria_despesakey = dm_categoria_despesa.key " \
                    "INNER JOIN dm_tempo " \
                    "on dm_tempo.key = tempokey " \
                    "WHERE AnoExercicio = {AnoExercicio} " \
                    "GROUP BY nome " \
                    "ORDER BY quantidade DESC;"

# Pesquisa por categorias de despesas, filtradas por despesas
query4_filter_despesa = "SELECT COUNT(dm_categoria_despesa.nome) AS quantidade, dm_categoria_despesa.nome AS categoria " \
                        "from dm_categoria_despesa " \
                        "INNER JOIN ft_pagamento " \
                        "on categoria_despesakey = dm_categoria_despesa.key " \
                        "INNER JOIN dm_despesa " \
                        "on dm_despesa.key = despesakey " \
                        "WHERE dm_despesa.nome = '{despesa}' " \
                        "GROUP BY dm_categoria_despesa.nome " \
                        "ORDER BY quantidade DESC;"

query5 = "SELECT dm_despesa.nome AS Despesa, count(dm_despesa.nome) AS Quantidade " \
         "from dm_despesa " \
         "INNER JOIN ft_pagamento " \
         "on despesakey = dm_despesa.key " \
         "GROUP BY Despesa " \
         "ORDER BY quantidade DESC;"

# query5_filter_despesa = "SELECT dm_despesa.nome AS Despesa, count(dm_despesa.nome) AS Quantidade " \
#          "from dm_despesa " \
#          "INNER JOIN ft_pagamento " \
#          "on despesakey = dm_despesa.key " \
#          "WHERE despesa = {despesa} " \
#          "GROUP BY Despesa " \
#          "ORDER BY quantidade DESC;"

query5_filter_ano = "SELECT dm_despesa.nome AS Despesa, count(dm_despesa.nome) AS Quantidade " \
         "from dm_despesa " \
         "INNER JOIN ft_pagamento " \
         "on despesakey = dm_despesa.key " \
         "INNER JOIN dm_tempo " \
         "on dm_tempo.key = tempokey " \
         "WHERE AnoExercicio = {AnoExercicio} " \
         "GROUP BY Despesa " \
         "ORDER BY Quantidade DESC;"

# query5_filter = "SELECT dm_despesa.nome AS Despesa, count(dm_despesa.nome) AS Quantidade " \
#          "from dm_despesa " \
#          "INNER JOIN ft_pagamento " \
#          "on despesakey = dm_despesa.key " \
#          "INNER JOIN dm_tempo " \
#          "on dm_tempo.key = tempokey " \
#          "WHERE AnoExercicio = {AnoExercicio} " \
#          "AND Despesa = {despesa}" \
#          "GROUP BY Despesa " \
#          "ORDER BY quantidade DESC;"

query_anos = "SELECT AnoExercicio from dm_tempo GROUP BY AnoExercicio;"

query_despesas = "SELECT nome from dm_despesa GROUP BY nome;"