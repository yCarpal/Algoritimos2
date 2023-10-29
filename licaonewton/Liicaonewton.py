def calcular_raiz_quadrada(numero, precisao=1e-6):
    if numero < 0:
        return None  # Lidando com números negativos (raiz quadrada não real)

    aproximacao = numero  # Comece com uma estimativa inicial
    while abs(aproximacao * aproximacao - numero) > precisao:
        aproximacao = 0.5 * (aproximacao + numero / aproximacao)

    return aproximacao


numero = float(input("Insira um número para calcular a raiz quadrada: "))  # Número para calcular a raiz quadrada
raiz_quadrada = calcular_raiz_quadrada(numero)
print(f"A raiz quadrada de {numero} é aproximadamente {raiz_quadrada:.6f}")