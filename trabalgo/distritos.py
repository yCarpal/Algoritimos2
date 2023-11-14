def Traco(txt):
    print('-'*30)
    print(txt)
    print('-'*30)
    

def contar_orgaos_do_distrito(distrito):
    contador = 0
    with open("trabalgo/aquaviario.csv", "r") as arquivo:
        linhas = arquivo.readlines()
        for i in linhas[1:]:  # Ignora a primeira linha
            campos = i.strip().split(',') # remove os espaços vazios e separa por virgula
            if campos[0] == distrito: # se a coluna 0 for igual ao distrito selecionado
                contador += 1 # adiciona o orgão no terminal
    return contador

def listar_orgaos_do_distrito(distrito):
    with open("trabalgo/aquaviario.csv", "r") as arquivo:
        linhas = arquivo.readlines() # ler o arquivo criando a variavel linhas
        for i in linhas[1:]:  # Ignora a primeira linha  # em cada i nas linhas do arquivo ele vai 
            campos = i.strip().split(',') # remove os espaços vazios e separa por virgula
            if campos[0] == distrito: # se a coluna 0 for igual ao distrito selecionado
                print(f"O Distrito {distrito} possui o orgão {campos[1]}, na região de {campos[2]}") # ira mostrar no terminal

# Código principal
while True:
    Traco("Menu de Opções:")
    Traco("1. Contar órgãos do distrito")
    Traco("2. Listar órgãos do distrito")
    Traco("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1": 
        distrito = input('Digite o número do distrito (de 1 a 9) para contar os órgãos do aquaviário: ')
        if distrito not in map(str, range(1, 10)):
            print('Número de distrito não está no arquivo')
        else:
            contador = contar_orgaos_do_distrito(distrito)
            print(f'Total de órgãos no Distrito {distrito}: {contador}')
    elif opcao == "2":
        distrito = input('Digite o número do distrito (de 1 a 9) para listar os órgãos do aquaviário: ')
        if distrito not in map(str, range(1, 10)):
            print('Número de distrito não está no arquivo')
        else:
            listar_orgaos_do_distrito(distrito)
    elif opcao == "3":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")