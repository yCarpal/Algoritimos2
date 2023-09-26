#  Faça um programa que faça a leitura e armazene 10 valores inteiros em
# uma estrutura (array, lista, tupla ou conjunto). Mostre quais os valores armazenados
# são menores ou iguais a 0 e suas respectivas posições. O programa deverá informar
# se não houver nenhum número armazenado nessa condição.

# irei fazer em array

import numpy as np

x = 10
valores = np.zeros(x)


for i in range(10):
    valor = int(input("Informe um valor para x: "))
    valores[i] = valor

print(valores)



for i in range(x):
    if valores[i] < 0:
       print(f"Valor {valores[i]} na posição {i} é menor que zero")
    elif valores[i] == 0:
        print(f"Esse valor {valores[i]} na posição {i} é igual a zero")
    elif valores[i] > 0:
        print(f"Valor {valores[i]} na posição {i} não é menor que zero")
    

for valor in valores:
    if valor <= 0:
        print("Possui alguns valores iguais a zero e menores que zero")
        break
else:
    print("Todos os valores são maiores que zero.")
    