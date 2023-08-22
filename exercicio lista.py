import numpy as np
x= [0,0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    x[i] = int(input(f"informe o valor do indice {i}: "))

for i in range(10):
    if (x[i] %2 == 0):
        x[i] = x[i] *i
    else:
        x[i]=i

print(x)
