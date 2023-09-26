# (2,0 pontos) Faça um algoritmo que preencha um variável (array, lista, tupla ou
# conjunto) com 8 números inteiros, calcule e mostre as duas variáveis (array, lista,
# tupla ou conjunto) resultantes. A primeira variável deve conter os números positivos
# e o segundo, os números negativos informados pelo usuário. Cada variável de
# resultado terá, no máximo, oito posições, que poderão ou não ser utilizadas. No caso
# do valor 0, este não deverá ser incluído nas variáveis de resultado

n = 8
valores = []
lista_posit = []
lista_negat = []

for i in range(n):
    valor = int(input(f"Insira um valor para a lista: "))
    valores.append(valor)

lista_sem_0 = []
for valor in valores:
    if valor != 0:
        lista_sem_0.append(valor)

for valor in lista_sem_0:
    if valor < 0:
        lista_negat.append(valor)
    elif valor > 0:
        lista_posit.append(valor)

print(f"Os valores lista_posit na lista 1 são: {lista_posit} ja os valores negativos na lista 2 são: {lista_negat}")