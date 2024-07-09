# def pa_naturais(n):
#     an = 0 + (n - 1) * 1
#     print(an)

# pa_naturais(5)

# def pa_naturais_sequencia(m):
#     for i in range (1, m+1):
#         an = 0 + (i - 1)*1
#         print (an)

# pa_naturais_sequencia(100)

# a = int(input('Digite um numero: '))
# b = int(input('Digite o segundo numero: '))
# while a < b:
#     a=int(input('Digite o primeiro número novamente: '))
# y = a-b

# print(y)

# Nomes = ['Ana', 'João', 'Maria', 'Carlos', 'Beatriz', 'Paulo', 'Sofia', 'Lucas', 'Fernanda', 'Ricardo', 'Aline', 'Marcelo', 'Helena', 'Bruno', 'Carolina']
# Idades = [25, 30, 22, 28, 35, 27, 24, 31, 29, 26, 32, 33, 23, 34, 21]
# Peso =[60, 75, 55, 68, 80, 70, 62, 77, 65, 73, 58, 76, 63, 72, 61]


import matplotlib.pyplot as plt #[Bliblioteca para visualização de dados no pyton]

# Nomes = ['Ana', 'João', 'Maria', 'Carlos', 'Beatriz', 'Paulo', 'Sofia', 'Lucas', 'Fernanda', 'Ricardo', 'Aline', 'Marcelo', 'Helena', 'Bruno', 'Carolina']
# Idades = [25, 30, 22, 28, 35, 27, 24, 31, 29, 26, 32, 33, 23, 34, 21]
# Peso =[60, 75, 55, 68, 80, 70, 62, 77, 65, 73, 58, 76, 63, 72, 61]

# plt.scatter(Idades, Peso) #cria um gráfico de dispesão usando os dados anteriores

# for nomes_cont, idades_count, peso_count in zip(Nomes, Idades, Peso):
#     plt.annotate(nomes_cont, xy= (idades_count, peso_count), xytext=(5, -5), textcoords='offset points')
# plt.title('Idades x Peso')
# # plt.xlabel('Idades')
# # plt.ylabel('Peso')
# # plt.show()

# from random import *

# x = []
# for i in range (0,20):
#     z = round(float(uniform(0.,10.10)))
#     x.append(z)

# print(x)

# y = []
# for i in range (0,20):
#     z = round(int(uniform(0,100)))
#     y.append(z)

# print(y)

# z = x,y
# import pandas as pd 
# df = pd.DataFrame (z, index=['x', 'y']).T
# print(df)

# plt.hist(df.x)
# plt.show()