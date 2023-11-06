A = 1
B = float(input("Informe o valor para B:"))

Med_HAR = 0
Med_ari = 0
Med_geo = 0

count = 0

while count <= 3:
    Med_HAR = (2*A*B)/(A+B)
    Med_ari = (A+B)/2
    A = Med_HAR
    B = Med_ari
    Med_geo = (A*B)**0,5
    count += 1

print(F"A média harmonica é {Med_HAR}, a média geométrica é {Med_geo} e a média aritmética é {Med_ari}")