# Faça um programa que crie um arquivo texto e que salve seu nome
# neste arquivo, após sobrescreva o conteúdo deste arquivo com a frase “Eu amo
# algoritmos!”.

nome = input("Insira o seu nome : ")
frase = "\n Eu amo algoritmos"

with open("manipulacao/exercicios/nome.txt","w") as exercicio:
    exercicio.write(nome)

with open("manipulacao/exercicios/nome.txt", "a") as exercicio:
    exercicio.write(frase)

print(f"O Nome {nome}, e a Frase {frase} foi salvo no arquivo 'nome.txt'")
