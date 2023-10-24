# Faça um programa que preencha um vetor com 9 números inteiros, calcule e
# mostre os que são números primos e suas respectivas posições.


V = []

N = 3

for i in range(N):
    V.append(int(input(f"Digite um valor para a posição [{i}]: ")))

for i in range(N):
    cont = 0

    for x in range(1, V, [i]):
        if (V[i] % x == 0):
            cont += 1
    if cont == 1:
        print(f"O número {V[i]} na posição {i} é impar.")
