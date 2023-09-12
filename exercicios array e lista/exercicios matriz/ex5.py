# Matriz = []

# for l in range(10):
#     for c in range(10):
#         Matriz[l][c] = int(input(f"insira valores para [{l},{c}]"))
# print('-='*50)

# for l in range(10):
#     for c in range(10):
#         print(f"[{Matriz[l][c]:^2}]", end='')

# coluna = 1
# soma_col_2 = sum(Matriz[coluna])
# for i in range(0, 5):
#     print(Matriz[i][i], end=" ")
# soma_diagonal = sum(Matriz[i][i])
# print()
# print(f"A soma dos valores da segunda coluna é : {soma_col_2}, e a soma dos valores da diagonal são: {soma_diagonal}")
# Inicialize a matriz
import numpy as np 

Matriz = []
# Lendo valores para a matriz
Matriz = np.random.randint(100, size=(10, 10)) 
print('-='*50)

# Mostrando a matriz
for l in range(10):
    for c in range(10):
        print(f"[{Matriz[l][c]:^2}]", end='')
    print()  # Pula para a próxima linha após imprimir uma linha completa

coluna = 1
soma_col_2 = sum(Matriz[i][coluna] for i in range(10))

# Calculando a soma da diagonal principal
soma_diagonal = sum(Matriz[i][i] for i in range(10))

print()
print(f"A soma dos valores da segunda coluna é: {soma_col_2}, e a soma dos valores da diagonal é: {soma_diagonal}")
