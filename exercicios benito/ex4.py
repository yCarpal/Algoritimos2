inicio = 1
final = 1000000
lista = []

for i in range(inicio, final + 1):
    if i > 1:
        for n in range(2, i):
            if (i % n) == 0:
                break
        else:
            lista.append(i)
                       
print(len(lista))