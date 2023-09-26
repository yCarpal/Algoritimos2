
import numpy as np

v = np.zeros(5)

for i in range(5): # 0,1,2,3,4
    v[i] = float(input("Numero qualquer: "))

for i in range(0,5,1):
    x = v[i]
    if x % 2 == 0:
        print(f"{x} é par")
    
print(v)