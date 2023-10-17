# Escreva um algoritmo que leia um valor para X e uma sub-rotina que imprima todos os números ímpares do intervalo fechado de 1 a X.

#Primeira maneira de fazer

def impares(x: int):
    """IMprima os ímpares de 1 até x"""
    for i in range(1,x+1):
        if i % 2 != 0:
            print(i)


# Segunda maneira

def impares2(x: int):
    """Imprima os ímpares de 1 até x"""
    for i in range(1,x+1,2):
        print(i)