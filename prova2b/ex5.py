# 5) (2,0 pontos) Faça um programa que leia um vetor de 3 posições e uma matriz de 3 x
# 3 calcule e mostre o resultado da multiplicação do primeiro item do vetor, por toda a
# primeira coluna da matriz, do segundo item do vetor por toda a segunda coluna da
# matriz e assim sucessivamente e armazene os resultados linha a linha na matriz
# resultado.
vetor = [1,2,3]
print("O vetor é :")
print(vetor)

print("-="*30)

N = 3
M = []
Matriz_R = []
for l in range(N):
    linha = []
    for c in range(N):
        valor = int(input(f"Insira valores para [{l},{c}]: "))
        linha.append(valor)
    M.append(linha)

print("-="*30)

print("A demonstração da matiz é : ")
for l in range(N):
    for c in range(N):
        print(f"[{M[l][c]:^2}]",end='')
    print()

for l in range(N):
    linha = []
    for c in range(N):
        linha.append(vetor[l] * M[l][c])
    Matriz_R.append(linha)
print("A matriz com os resultados multipilcados :")
print(Matriz_R)



