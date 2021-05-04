import pandas as pd

dataPath = 'dados/dados_experimentos.zip'
dados = pd.read_csv(dataPath, compression = 'zip')

# print(dados)
# print(dados.shape)

# print(dados['tratamento'].unique())
# print(dados['tempo'].unique())
# print(dados['dose'].unique())
# print(dados['droga'].unique())

# 28 minutos 
# https://www.alura.com.br/imersao-dados/aula01-python-pandas-farmacologia?utm_campaign=imersao_dados_3_aulas_aula_1&utm_medium=email&utm_source=RD+Station