matriz = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for l in range(0,5):
    for c in range(0,5):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]:"))
print('-='*50)

for l in range(0,5):
    for c in range(0,5):
        print(f"[{matriz[l][c]:^2}]", end='')
    print()

linha = 3
soma_linha_4 = sum(matriz[linha])

print(f"A soma dos valores da linha 4 é :{soma_linha_4}")
