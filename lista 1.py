l1 = []
l2 = []
l3 = []

for i in range(0 , 5):
    l1.append(int(input(f"l1 - valor indice {i}: ")))

for i in range(0 , 5):
    l2.append(int(input(f"l2 - valor indice {i}: ")))

print(l1)
print(l2)

for i in range(0, 5):
    l3.append(l1[i] + l2[i])

print(l3)
