# import numpy as np
# tamanho=4
# linha=np.empty((tamanho))
# for t in range (tamanho):
#     valor=(float(input('Informe os valores que serão adicionados: ')))
#     linha[t]=valor #Tem sempre que informar a posição a qual vou adicionar
# print(linha)
# inverso=linha[::-1] # para eu fazer o inverso 
# print('O inverso é :  ')
# print(inverso)


# soma_lista=sum(linha)
# print('A soma dos valores da lista é : ')
# print(soma_lista)
# print('A media dos valores da lista é : ')
# print(soma_lista/2)


# '''Faça um algoritmo que lê 5 valores para uma variável do tipo vetor e determine o maior e o menor valor armazenado no vetor.'''
# maior=max(linha)
# print('O maior valor digitado  é: ')
# print(maior)
# menor=min(linha)
# print('O menor valor digitado é: ')
# print(menor)

# posicoes_maior = [i for i, valor in enumerate(linha) if valor == maior]
# print(f'As posições onde está o maior valor {maior} é : {posicoes_maior}')#procure a posição i em i onde o valor é mair, poderia ter usado até em matriz mas como é um ixi ou seja não é listas de listas ta ok 
# #OU PODE FAZER COM NUMPRY:
# # Encontrar as posições onde o maior valor ocorre no array
# posicoes = np.where(linha == maior)[0]

# # Imprimir o maior valor e suas posições
# print(f'O maior valor é {maior} e está nas posições: {posicoes}')

tamanho = 4
lista = []

for t in range(tamanho):
    valor = float(input('Informe os valores que serão adicionados: '))
    lista.append(valor)

print(lista)

inverso = lista[::-1]

print('O inverso é:')
print(inverso)

soma_lista = sum(lista)
#ou
# soma_lista = 0

# for valor in lista:
#     soma_lista += valor
print('A soma dos valores da lista é:')
print(soma_lista)
print('A média dos valores da lista é:')
print(soma_lista / tamanho)

maior = lista[0]
menor = lista[0]

for valor in lista:
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor

print('O maior valor digitado é:')
print(maior)

print('O menor valor digitado é:')
print(menor)

posicoes_maior = [i for i, valor in enumerate(lista) if valor == maior]
print(f'As posições onde está o maior valor {maior} são: {posicoes_maior}')