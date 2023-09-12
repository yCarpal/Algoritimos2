# Faça um algoritimo que leia a idade de uma pessoa
# e apresente a mesma expressa em dias


"""
entradas-  idade em anos
processamento - multiplicar por 365
saida - idade em dias
"""

idade = int(input("informe a idade em anos:"))
ano_dias = 365
idade_em_dias = idade*ano_dias


if idade_em_dias > 10000:
    print(" você ja viveu mais que 10.000 dias")
else:
    print("jovem")
    

print(f" a idade corresponde a {idade_em_dias} dias")
