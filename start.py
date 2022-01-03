import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# seta o tamanho dos graficos
plt.figure(figsize=(10, 8))

# seta o sns para os graficos ficarem estilizados
sns.set()

dataPath = 'dados/dados_experimentos.zip'
dados = pd.read_csv(dataPath, compression='zip')

# print(dados)
# print(dados.shape)

# print(dados['tratamento'].unique())
# print(dados['tempo'].unique())
# print(dados['dose'].unique())
# print(dados['droga'].unique())

# print(dados['g-0'].unique())

# print(dados['tratamento'].value_counts())
# print(dados['dose'].value_counts())

# print(dados['tratamento'].value_counts(normalize = True)) # Pega a porcentagem do dados
# print(dados['tratamento'].value_counts().plot.pie())

# dados['tratamento'].value_counts().plot.pie().figure.savefig('charts/pie.png') # salva em png em pizza
# dados['tempo'].value_counts().plot.bar().figure.savefig('charts/bar.png') # salva em png em barras

# print(dados[dados['g-0'] > 0]) # Pegando somente as 'g-0' que são maiores que 0

# dados_filtrados = dados[dados['g-0'] > 0]
# print(dados_filtrados)


# renomeia a coluna droga para composto
dados.rename(columns={'droga': 'composto'}, inplace=True)

#### 
# Pegando as 5 primeiros compostos da lista de compostos unicos
# top_compostos = dados['composto'].value_counts().index[:5]

# o @ na string abaixo é para avisar a query qye top_compostos é uma veriavel já setada no código sem a necessidade de interpolação de string
# ax = sns.countplot(x='composto', data=dados.query('composto in @top_compostos'))
# ax.set_title('Top5 compostos').figure.savefig("output.png")

# print(f'O valor de pi é {pi: >10.3}') # Interpolação de string!
#### 

# print(dados['g-0'].min())
# print(dados['g-0'].max())

dados['g-0'].hist(bins=50)


# 41 minutos