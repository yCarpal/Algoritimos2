def calcular_raiz_quadrada(numero, iteracoes=):
    xk = numero / 2  # Suposição inicial (pode ser qualquer valor razoável)
    
    for _ in range(iteracoes):
        xk = 0.5 * (xk + numero / xk)  # Fórmula de iteração

    return xk

# Exemplo de uso
numero = float(input("Insira um número para calcular a raiz: "))  # Número para calcular a raiz quadrada
raiz_quadrada = calcular_raiz_quadrada(numero) #inserindo a função
print(f"A raiz quadrada de {numero} é aproximadamente {raiz_quadrada:.6f}")
