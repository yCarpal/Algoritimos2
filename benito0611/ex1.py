from datetime import datetime

inicio = datetime.now().microsecond
iteracoes = 0
def raizq(x):
    global iteracoes
    if (valor/2)**2 == valor:
        return valor/2
    else: 
        if x == valor:
            x = 1 
            while true:
                iteracoes += 1
                f = x**2 - valor
                f_linha = 2*x
                resultado = x - (f/f_linha)
                if abs(resultado-x)<= 0.1:
                    return resultadoelse:
                else: 
                    return raizq(resultado)

valor = 3 
print(f"Araiz de {valor} é {raiz(valor)}")
print(f"Foram feitas {iteracoes} iterações.")
print(f"Otempo de execução do código foi de {abs(inicio - datetime.now().microsecond)}microssegundos")