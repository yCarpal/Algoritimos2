n = int(input("Insira um número: "))
multiplo = 0
for k in range(1, n+1):
    if k % n == 0:
        print("Multiplo de {k}")
        multiplo += 1

if multiplo == 1 :
    print("É primo")
else:
    print("Não é primo")