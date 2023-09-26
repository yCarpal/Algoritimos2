# Elabore um programa que preencha uma estrutura (array, lista, tupla ou
# conjunto), com 18 elementos calcule e mostre:
# a) O maior valor armazenado na estrutura e a sua respectiva posição;
# b) O menor valor armazenado na estrutura e a sua respectiva posição;

lista = []

for i in range(19):
    valor = float(input(f"Qual valor deseja armazenar na posição L[{i}]? "))
    lista.append(valor)

maxindex = 0
minindex = 0
maior_valor = 0
menor_valor = 0

for i in range(19):
    if (i == 0):
        maxindex = i
        minindex = i
    elif (lista[i] > lista[maxindex]):
        maxindex = i
    elif (lista[i] < lista[minindex]):
        minindex = i

for i in range(19):
    if (i == 0):
        maior_valor= lista[i]
        menor_valor = lista[i]
    elif (lista[i] > maior_valor):
        maior_valor = lista[i]
    elif (lista[i] < menor_valor):
        menor_valor = lista[i]

print(lista)
print(f"O maior valor :{maior_valor} esta armazenado no índice: {maxindex} ")
print(f"O menor valor :{menor_valor} esta armazenado no índice: {minindex} ")


