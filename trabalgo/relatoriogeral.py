def Traco(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

def relatorio(nome_arquivo, conteudo):
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(conteudo)

def contar_orgaos_do_distrito(distrito):
    contador = 0
    with open("trabalgo/aquaviario.csv", "r") as distritos:
        linhas = distritos.readlines()
        for i in linhas[1:]:
            campos = i.strip().split(',')
            if campos[0] == distrito:
                contador += 1
    resultado = f'O Número total de órgãos no Distrito {distrito} é de {contador}\n'
    relatorio("distritos.txt", resultado)
    return contador

def listar_orgaos_do_distrito(distrito):
    with open("trabalgo/aquaviario.csv", "r") as distritos:
        linhas = distritos.readlines()
        for i in linhas[1:]:
            campos = i.strip().split(',')
            if campos[0] == distrito:
                resultado = f'O Distrito {distrito} possui o orgão {campos[1]}, na região de {campos[2]}\n'
                relatorio("distritos.txt", resultado)
                print(resultado)

# Código principal
while True:
    Traco("Menu de opções:")
    Traco("1. Contar órgãos do distrito")
    Traco("2. Listar órgãos do distrito")
    Traco("3. Sair do Sistema")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        distrito = input('Digite o número do distrito (de 1 a 9) para contar os órgãos do aquaviário: ')
        if distrito not in map(str, range(1, 10)):
            print('Número de distrito não está no arquivo')
        else:
            contador = contar_orgaos_do_distrito(distrito)
            print(f'O Número total de órgãos no Distrito {distrito} é de {contador}')
    elif opcao == "2":
        distrito = input('Digite o número do distrito (de 1 a 9) para listar os órgãos do aquaviário: ')
        if distrito not in map(str, range(1, 10)):
            print('Número de distrito não está no arquivo')
        else:
            listar_orgaos_do_distrito(distrito)
    elif opcao == "3":
        print("Saindo do programa, tenha um bom dia!!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")