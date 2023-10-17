# 3) (2,0 pontos) Faça um algoritmo com 100 valores armazenados em uma variável x
# (array, lista, tupla ou conjunto). Calcular e mostrar no final:
# ● a quantidade de valores pares armazenados em x.
# ● e a média dos valores impares armazenados em x.

N = 100
tamanho = N
x = []
num_pares = 0
soma_impares = 0
num_impares = 0

for i in range(N):
    valor = int(input("Insira valores para a lista: "))
    x.append(valor)
print(x)
print("-="*30)

for valor in x:
    if valor % 2 == 0: 
        num_pares = num_pares + 1
    else:
        soma_impares = soma_impares + valor
        num_impares = num_impares + 1

if num_impares > 0:
    media_impares = soma_impares/num_impares
else:
    media_impares = 0

print('-='*30)
print(f"Quantidade de números pares: {num_pares} e a Média dos valores ímpares é de: {media_impares}")



        


