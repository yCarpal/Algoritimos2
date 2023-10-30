def calcular_raiz_quadrada(numero, iteracoes = 1e-6 ):
    xk = numero / 2  # Suposição inicial (pode ser qualquer valor razoável)
    
    max_iteracoes = int(1e6)  # Número máximo de iterações (evita um loop infinito)
    
    for _ in range(max_iteracoes):
        xk_novo = 0.5 * (xk + numero / xk)  # Fórmula de iteração

        if (xk_novo * xk_novo - numero) * (xk_novo * xk_novo - numero) <= iteracoes * iteracoes:
            return xk_novo  # Se a tolerância for atingida, retornamos o valor

        xk = xk_novo  # Atualiza o valor de xk


numero = float(input("Insira um número para calcular a raiz: "))  # Número para calcular a raiz quadrada
raiz_quadrada = calcular_raiz_quadrada(numero) #inserindo a função
print(f"A raiz quadrada de {numero} é aproximadamente {raiz_quadrada:.6f}")
