# Escreva um algoritmo que imprima todos os números inteiros de 10 a 1 (em ordem decrescente), utilizando recursividade.

def imprime(n):
    print(n)
    if n !=1:
        imprime(n-1)
        
imprime(9)