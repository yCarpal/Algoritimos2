# 4) (2,0 pontos) Faça um algoritmo que preencha uma matriz 6 x 6 com números
# inteiros, execute as trocas especificadas a seguir e mostre a matriz resultante:
# ● A linha de índice 1 com a linha de índice 4;
# ● A coluna de índice 3 com a coluna de índice 5;

N = 6

M = []

for l in range(N):
    linha = []
    for c in range(N):
        valor = int(input(f"Insira valores para [{l},{c}]: "))
        linha.append(valor)
    M.append(linha)

print("-="*30)

print("A demonstração da matriz é : ")
for l in range(N):
    for c in range(N):
        print(f"[{M[l][c]:^2}]",end='')
    print()

for i in range(N):
    aux = M[1][i]
    M[1][i] = M[4][i]
    M[4][i] = aux

for i in range(N):
    aux = M[i][3]
    M[i][3] = M[i][5]        
    M[i][5] = aux
print("Apos as trocas esta é a matriz final:")
print(M)

