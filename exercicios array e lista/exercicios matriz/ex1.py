# matriz = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

# for l in range(0,5):
#     for c in range(0,5):
#         matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]:"))
# print('-='*50)

# for l in range(0,5):
#     for c in range(0,5):
#         print(f"[{matriz[l][c]:^2}]", end='')
#     print()

M = []

# Lendo os valores para a matriz
print("Digite os valores da matriz 5x5:")

for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    M.append(linha)

# Mostrando a matriz digitada
print("\nValores digitados para a matriz M:")
for i in range(5):
    for j in range(5):
        print(M[i][j])