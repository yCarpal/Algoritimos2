def raiz_primos(valor):
    raiz_q = round(valor**(0.5))
    primos = []
    for x in range(2, raiz_q):
        divisores = 0

        for y in range(2, x):
            if x % y == 0:
                divisores += 1
                break
        
        if divisores == 0:
            primos.append(x)

    return primos


def todos_primos(valor):
    inicial = raiz_primos(valor)
    total_primos = [x for x in inicial]

    for x in range(2, valor + 1):
        divisores = 0

        for y in inicial:
            if x % y == 0:
                divisores += 1
                break
        
        if divisores == 0:
            total_primos.append(x)
    
    return print(f'Todos os primos: {total_primos}\n Total de primos: {(len(total_primos))} \n Maior número primo do intervalor: {total_primos[-1]}')\
            

valor = int(input('Digite um valor: '))
todos_primos(valor)