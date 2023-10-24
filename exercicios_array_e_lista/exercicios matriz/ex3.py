matriz = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for l in range(0,5):
    for c in range(0,5):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]:"))
print('-='*50)

for l in range(0,5):
    for c in range(0,5):
        print(f"[{matriz[l][c]:^2}]", end='')
    print()
print("Os valores da diagonal principal são:")
for i in range(0,5):
    print(matriz[i][i], end=" ")
print()