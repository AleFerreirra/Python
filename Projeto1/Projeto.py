import pandas as pd
import matplotlib as plt
import seaborn as sns
import csv
import pylab as pl


# Carregamento do dataset
with open ('Projeto1/ecommerce_product_dataset.csv') as csvFile:
    df = pd.read_csv(csvFile)

# Exibir as primeiras linhas do dataset
print((df.head()))

# Verificar valores ausentes
valAusente = df.isnull().sum()

#remover duplicadas
df.drop_duplicates(inplace=True)

# Resumo das informações do dataset
df.info()

# Mostrar os valores ausentes
valAusente

# Configuração dos estilos dos gráficos
sns.set(style='whitegrid', palette='muted')

#Plotagem da distribuição de preços
pl.figure(figsize=(12, 6))
sns.histplot(df['Price'], bins=30, kde=True, color='blue')
pl.title('Distribuição de Preços dos Produtos', fontsize=16)
pl.xlabel('Preço', fontsize=14)
pl.ylabel('Frequência', fontsize=14)
pl.show()


# # Plotagem das vendas por categoria de produto
pl.figure(figsize=(14, 7))
sns.countplot(data=df, x='Category', order=df['Category'].value_counts().index, palette='viridis')
pl.title('Vendas por Categoria de Produto', fontsize=16)
pl.xlabel('Categoria', fontsize=14)
pl.ylabel('Contagem de Vendas', fontsize=14)
pl.xticks(rotation=45, fontsize=12)
pl.yticks(fontsize=12)
pl.show()


#Plotagem da relação entre preço e avaliação dos produtos
pl.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Price', y='Rating', hue='Category', palette='viridis', alpha=0.7)
pl.title('Relação entre Preço e Avaliação dos Produtos', fontsize=16)
pl.xlabel('Preço', fontsize=14)
pl.ylabel('Avaliação', fontsize=14)
pl.legend(title='Categoria', bbox_to_anchor=(1.05, 1), loc='upper left')
pl.show()




