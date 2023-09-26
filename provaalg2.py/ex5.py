# (2,0 pontos) Na Teoria de Sistemas define-se como elemento minimax de uma
# matriz o menor elemento da linha em que se encontra o maior elemento da matriz.
# Escreva um programa que preencha uma matriz M5x5 após sua leitura, determine o
# seu elemento minimax

matriz = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for l in range(0,5):
    for c in range(0,5):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]:"))
print('-='*50)

for l in range(0,5):
    for c in range(0,5):
        print(f"[{matriz[l][c]:^2}]", end='')
    print()

maior_elemento = matriz[0][0]
for linha in matriz:
    for elemento in linha:
        if elemento > maior_elemento:
            maior_elemento = elemento

# Encontrar o elemento minimax na linha do maior elemento
linha_maior_elemento = matriz[0]
for linha in matriz:
    if maior_elemento in linha:
        linha_maior_elemento = linha
        break

elemento_minimax = min(linha_maior_elemento)

print(f"O elemento minimax da matriz é: {elemento_minimax}")

