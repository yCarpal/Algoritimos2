qualquer = int(input("Informe o número de parada: "))
Divisores = []
V = []
primo = False
cont = 0

raiz = qualquer**0.5

RaizInteira = int(raiz)

for j in range (2, RaizInteira+1):
    mult = 0
    for i in range(2, j):
        if j % i == 0:
            mult +=1
            break
    if mult == 0:
        V.append(j)

print("Os primos até a raiz inteira é: ", V)

for l in V:
    if qualquer % l == 0:
        Divisores.append(l)
        cont += 1

print(f"A raiz inteira é: {RaizInteira}")

if cont > 0:
    print(f"O número {qualquer} não é primo pois é divisivel por:")
    print(Divisores)
else:
    print(f"O número {qualquer} é um número primo!")