# Faça um programa que crie um arquivo texto e que salve seu nome neste arquivo (o nome deve ser  informado via terminal).

nome = input("Digito o seu nome:")

with open("manipulacao/exercicios/nome.txt", "w") as exercicio:
    exercicio.write(nome)

print(f"O Nome {nome}, foi salvo em no arquivo 'nome.txt'")
