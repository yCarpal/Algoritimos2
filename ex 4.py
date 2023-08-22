# #Altere o algoritmo anterior para que ele realize o produto da primeira lista, pelo
# inverso da segunda lista.

l1 = []
l2 = []
l3 = []
N = 5

for i in range(0 , N):
    l1.append(int(input(f"l1 - valor indice {i}: ")))
    
for i in range(0 ,  N):
    l2.append(int(input(f"l2 - valor indice {i}: ")))

#CRIAÇÃO DOS VETORES
for i in range(N):
    j = N-1-i #indice do segundo vetor
    x = l1[1]* l2[j]
    l3.append(x)