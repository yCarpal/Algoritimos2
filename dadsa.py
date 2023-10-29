def calcular_raiz_quadrada(numero, precisao=1e-6):
    if numero < 0:
        return None  # Lidando com números negativos (raiz quadrada não real)

    aproximacao = numero  # Comece com uma estimativa inicial
    while True:
        estimativa_anterior = aproximacao
        aproximacao = 0.5 * (aproximacao + numero / aproximacao)  # Fórmula de Newton
        if abs(aproximacao - estimativa_anterior) < precisao:
            return aproximacao

# Exemplo de uso
numero = float(input("Insira um número"))  # Número para calcular a raiz quadrada
raiz_quadrada = calcular_raiz_quadrada(numero)
print(f"A raiz quadrada de {numero} é aproximadamente {raiz_quadrada:.6f}")