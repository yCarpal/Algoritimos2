
lista = []

for i in range(5):
    numero = int(input("Insira um número: "))
    lista.append(numero)

nome = input("Insira um nome para ser salvo no arquivo: ")

with open(nome, "w") as exercicios:
    for numero in lista:
        exercicios.write(str(numero) + "\n")

num_escritos = []
with open(nome, "r") as exercicio:
    for linha in exercicio:
        num_escritos.append(int(linha))

print(f"Os números lidos do arquivo {nome}:")
for numero in num_escritos:
    print(numero)





