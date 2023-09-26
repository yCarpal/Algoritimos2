# Faça um algoritmo que lê valores para duas (2) estruturas (array, lista,
# tupla ou conjunto) A e B com 3 elementos cada. Após apresente os valores lidos na
# ordem inversa. 


l1 = []
l2 = []


for i in range(3):
    l1.append(int(input("Insira um valor para lista: ")))
print(f"A lista 1 sera: {l1}")

for i in range(3):
    l2.append(int(input("Insira um valor para lista: ")))
print(l2)

l1.reverse()
l2.reverse()
print(f"A lista A no irverso será de : {l1} e a lista B no inverso será: {l2}")


