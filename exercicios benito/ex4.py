inicio = 1
final = 50

for i in range(inicio, final + 1):
    if i > 1:
        for n in range(2, i):
            if (i % n) == 0:
                break
        else:
            print(i)