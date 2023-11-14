# Desafio/Lista 5 (entrega 30/10): encontrar o melhor algoritmo para 
#calcular raiz quadrada de um número qualquer -> Sugestão: método de 
#newton
######### Método de newton seria naturalmente feito assim para uma raiz de 2
# import numpy as np

# f = lambda x: x**2 - 2
# f_prime = lambda x: 2*x
# newton_raphson = 1.4 - (f(1.4))/(f_prime(1.4))

# print("newton_raphson =", newton_raphson)
# print("sqrt(2) =", np.sqrt(2))

######## Para número qualquer
import time

def f(x, numero):
    return x ** 2 - numero
def f_prime(x):
    return 2 * x

def newton_sqrt(numero, iteracoes=10000, tolerancia=1e-6):
    atual = numero
    
    for i in range(iteracoes):
        proximo = atual - f(atual,numero) /f_prime(atual)
        atual = proximo
        print(proximo)

        if abs(f(atual,numero)) < tolerancia:
            return atual, i
    
    return atual, i

numero = float(input("Digite um número para calcular a raiz quadrada: "))
começo_time = time.time()
raiz_quadrada, i = newton_sqrt(numero)


print(f"A raiz quadrada de {numero} é aproximadamente {raiz_quadrada:.6f} em {i} inrerações.")
final_time = time.time()
total_time = final_time - começo_time
print(f"O total de tempo de execução é {total_time} segundos")
