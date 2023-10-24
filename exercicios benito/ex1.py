n = int(input("Insira um número:"))
lista_div = []
for i in range(1,n+1):
    if n % i == 0:
        lista_div.append(i)


print(lista_div)