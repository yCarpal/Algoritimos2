matriz = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for c in range(0,5):
    for l in range(0,5):
        matriz[c][l] = int(input(f"Digite um valor para [{c}, {l}]:"))
print('-='*50)

for l in range(0,5):
    for c in range(0,5):
        print(f"[{matriz[c][l]:^2}]", end='')
    print()




