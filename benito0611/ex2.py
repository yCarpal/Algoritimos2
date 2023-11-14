#Exercício 2) Faça um algoritmo que encontre a raiz quadrada de um número qualquer (por exemplo um 
# primo), usando o conceito da equivalência das médias aritméticas, geométrica e harmônica.

# import time

# val_a = float(input("Insira um valor para que seja calculada a raiz quadrada: "))
# val_b = float(input("Insira um valor para que seja calculada a raiz quadrada: "))

# start_time = time.time()

# med_aritm = 0
# med_geom = 0
# med_harm = 0
# dif = 1
# tolerancia = 1e-1
# contador = 0

# while dif > tolerancia:
#     med_harm = (2 * val_a * val_b)/(val_a + val_b)
#     med_aritm = (val_a + val_b)/2
#     val_a = med_harm
#     val_b = med_aritm
#     med_geom = ((val_a * val_b)**0.5)
#     contador += 1
#     dif = abs(med_aritm - med_harm)

#     # Verifique se a média geométrica é próxima o suficiente da média harmônica
#     if abs(med_geom - med_harm) < tolerancia:
#         break

# print(f"""Temos como valores finais de médias aritmética, geométrica e harmônica, os valores: 
# {med_aritm}, {med_geom}, {med_harm}. Foram necesárias {contador} interações para o cálculo.""")

# end_time = time.time()
# total_time = abs(end_time - start_time)
# print(f"O total de tempo de execução é {total_time:.20f} segundos")

import time
from mpmath import mp

mp.dps = 100 # Adjust the precision as needed

def calcular_medias(val_a, val_b, tolerancia=mp.mpf("1e-50")):
    med_aritm, med_geom, med_harm = 0, 0, 0
    contador = 0

    while True:
        med_harm = (2 * val_a * val_b) / (val_a + val_b)
        med_aritm = (val_a + val_b) / 2
        val_a, val_b = med_harm, med_aritm
        med_geom = mp.sqrt(val_a * val_b)
        contador += 1
        dif = mp.fabs(med_aritm - med_harm)

        if dif <= tolerancia:
            break

    return med_aritm, med_geom, med_harm, contador

val_a = mp.mpf(input("Insira um valor para calcular a raiz quadrada: "))
val_b = mp.mpf(input("Insira um valor para calcular a raiz quadrada: "))

start_time = time.time()
med_aritm, med_geom, med_harm, contador = calcular_medias(val_a, val_b)
end_time = time.time()
total_time = end_time - start_time

print(f"""Temos como valores finais de médias aritmética, geométrica e harmônica, os valores: 
{med_aritm}, {med_geom}, {med_harm}. Foram necessárias {contador} interações para o cálculo.""")
print(f"O total de tempo de execução é {total_time:.20f} segundos")
