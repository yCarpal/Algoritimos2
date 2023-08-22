l1 = []
l2 = []
l3 = []
N = 5

for i in range(N):
    l1.append(int(input(f"l1 - valor indice {i}: ")))

for i in range(N):
    l2.append(int(input(f"l2 - valor indice {i}: ")))
    
for i in range(N):
    l3.append(l1[i])

for i in range(N):
    l3.append(l2[i])
for i in range(10):
    print(l3)