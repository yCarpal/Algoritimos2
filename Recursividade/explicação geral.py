#Função recursiva do fatorial
def fatorial(n):
    if n == 0 or n == 1:
    return 1
    else:
        return n * fatorial(n-1)
a = int(input('informe um valor para obter o fatorial: '))
print("O resultado do fatorial é:",fatorial(a))