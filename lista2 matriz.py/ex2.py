# 2. Faça um algoritmo que lê uma matriz M10x10
# . Troque a seguir os valores
# contidos na linha de índice 2 com os da linha de índice 8 e também troque os
# valores da linha de índice 5 com os da coluna de índice 9. No final mostre a
# matriz
N = 10
Matriz = []

for l in range(N):
    linha = []
    for c in range(N):
        valor = int(input(f"Insira valores para [{l},{c}]: "))
        linha.append(valor)
    Matriz.append(linha)

print("-="*30)

print("A demonstração da matiz é : ")
for l in range(N):
    for c in range(N):
        print(f"[{Matriz[l][c]:^2}]",end='')
    print()
print("\nMatriz Após a troca de linhas:")
for i in range(N):
    Matriz[2], Matriz[8] = Matriz[8], Matriz[2]

for i in range(N):
    Matriz[5][i], Matriz[i][9] = Matriz[i][9], Matriz[5][i]

print("\nMatriz Após a troca da linha por coluna:")
for linha in Matriz:
    print(linha)


