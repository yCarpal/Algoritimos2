def calcular_raiz_quadrada(n):
    x = n / 2  # suposição inicial
    limite = 0.0001  # limite de diferença entre as estimativas consecutivas
    
    while True:
        estimativa_anterior = x
        x = (x + (n / x)) / 2
        diferenca = estimativa_anterior - x if estimativa_anterior > x else x - estimativa_anterior
        
        if diferenca < limite:
            break
    
    return x


numero = float(input("Insira um número para calcular a raiz: "))  # Número para calcular a raiz quadrada
raiz_quadrada = calcular_raiz_quadrada(numero)
print(f"A raiz quadrada de {numero} é aproximadamente {raiz_quadrada:.10f}")