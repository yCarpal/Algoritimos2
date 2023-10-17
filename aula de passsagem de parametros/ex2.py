#2.Faça uma sub-rotina que receba como parâmetro uma matriz(lista
#de lista) A[5][5] e retorne a soma de todos os seus elementos.

matriz = [[1,2,3,4,5],
     [2,3,4,5,6],
     [3,4,5,6,7],
     [4,5,6,7,8],
     [5,6,7,8,9]]

# maneira 1
def soma2(matriz: list):
    soma = 0 
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            soma += matriz [l][c]
    
    return soma

#Maneira 2

def soma(matriz: list):
    soma = 0
    for linha in matriz:
        for item in linha:
            soma  += item

    return soma


#Maneira 3

def  soma(matriz: list):
    soma = 0 
    for linha in matriz:
        soma += sum(linha)
    return soma

soma(matriz)