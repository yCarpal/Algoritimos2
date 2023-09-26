# Faça um algoritmo que receba um valor N correspondente ao tamanho de duas
# matrizes quadradas de ordem N (MNxN). Leia os valores inteiros para preencher
# todas as posições de cada uma das matrizes, e calcule a SOMA das matrizes.


N = int(input("Insira um valor para o N :"))
M1 = []
M2 = []


# Insira os valores da M1

for l in range(N):
    linha = []
    for c in range(N):
        valor = int(input(f"Insira valores para [{l},{c}:]: "))
        linha.append(valor)
    M1.append(linha)    
print("-="*30)

print("A Matriz 1 é :")
for l in range(N):
    for c in range(N):
        print(f"[{M1[l][c]:^2}]",end='')
    print()

#Insira os valores da M2
for l in range(N):
    linha = []
    for c in range(N):
        valor = int(input(f"Insira valores para [{l},{c}:]: "))
        linha.append(valor)
    M2.append(linha)
print("-="*30)

print("A matriz 2 é: ")
for l in range(N):
    for c in range(N):
        print(f"[{M2[l][c]:^2}]", end='')
    print()

#Aplique a soma das matrizes:

soma = []

for l in range(N):
    lin_soma = []
    for c in range(N):
        elem_soma = M1[l][c] + M2[l][c]
        lin_soma.append(elem_soma)
    soma.append(lin_soma)

#Monte a soma em formato de matriz:

print("-=" * 30)
print("A soma das matrizes é:")
for l in range(N):
    for c in range(N):
        print(f"[{soma[l][c]:^2}]", end='')
    print()