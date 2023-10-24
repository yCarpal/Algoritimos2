# Faça um algoritmo que lê valores para uma matriz M4X4 e um valor para a
# variável “a” (do tipo simples, pode ser: inteiro, float). Multiplicar cada valor
# contido na matriz pelo valor da variável e colocar os resultados num vetor(lista)
# V com 16 elementos. Mostre no final o vetor(lista).


N = int(input("Insira um valor para N: "))
Matriz = []
a = int(input("Insira um valor para o A :"))

for l in range(N):
    linha = []
    for c in range(N):
        valor = int(input(f"Insira valores para [{l},{c}]: "))
        linha.append(valor)
    Matriz.append(linha)

for l in range(N):
    for c in range(N):
        print(f"[{Matriz[l][c]:^2}]",end='')
    print()
    

V = []
for l in range(N):
    for c in range(N):
        mult = (Matriz[l][c]) * a
        linha.append(mult)
    V.append(mult)

print("O vetor é")
for i in V:
        print(V)

