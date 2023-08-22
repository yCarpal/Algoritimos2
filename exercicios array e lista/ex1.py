import numpy as np

V = [2,6,8,3,10,9,1,21,33,14]


X  = 2
Y = 4

print(V[X+1]) 
print(V[X+2]) 
print(V[X+3])
print(V[X*4])
print(V[X*1])
print(V[X*2])
print(V[X*3])
print(V[ V [X+Y]]) 
print(V[X+Y] )
print(V[8-V[2]]) 
print(f"V[V[4]], esta fora do range")
print(f"V[ V[ V[7]]], esta fora do range")
print(f"V[V[1]*V[4]], Esta fora do range")
print(V[X+4])
