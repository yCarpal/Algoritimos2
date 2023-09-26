# (2,0 pontos) Faça um programa que leia uma estrutura com 3 posições e uma
# matriz de 3 x 4. Troque a seguir os valores da estrutura pela coluna 1 da matriz.
# Após a troca, mostre a estrutura e a matriz.


# Criar uma estrutura com 3 posições (lista)
estrutura = [6, 6, 6]
print("estrutura antes da troca:")
print(estrutura)

# Inicializar uma matriz 3x4 com valores
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print("\nMatriz antes da troca: ")
for linha in matriz:
    print(linha)

# Trocar os valores da estrutura pela coluna 1 da matriz
for i in range(3):
    estrutura[i], matriz[i][0] = matriz[i][0], estrutura[i]

# Mostrar a estrutura e a matriz após a troca
print("Estrutura após a troca:")
print(estrutura)

print("\nMatriz após a troca:")
for linha in matriz:
    print(linha)

