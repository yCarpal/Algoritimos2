def Traco(txt):
    print('-'*30)
    print(txt)
    print('-'*30)
    

def filtrar_orgaos_por_estado(estado):
    contador = 0
    with open("trabalgo/aquaviario.csv", "r") as estados:
        linhas = estados.readlines()
        for i in linhas[1:]:  # Ignora a primeira linha
            campos = i.strip().split(',')
            if campos[2] == estado:
                contador += 1
    return contador

def listar_orgaos_por_estado(estado):
    orgaos = []
    with open("trabalgo/aquaviario.csv", "r") as estados:
        linhas = estados.readlines()
        for i in linhas[1:]:
            campos = i.strip().split(',')
            if campos[2] == estado:
                orgaos.append(campos[1])  # Adicione o órgão à lista
    return orgaos

def contar_estados_no_arquivo():
    estados_distintos = set()  # Conjunto para armazenar estados distintos

    with open("trabalgo/aquaviario.csv", "r") as estados:
        linhas = estados.readlines()
        for i in linhas[1:]:  # Ignora a primeira linha
            campos = i.strip().split(',')
            estado = campos[2]

            # Adicionar o estado aos estados distintos
            estados_distintos.add(estado)

    return len(estados_distintos)


arquivo_aquaviarios = "aquaviario.csv"

while True:
    Traco("Menu de Opções:")
    Traco("1. Contar órgãos por estado")
    Traco("2. Listar órgãos por estado")
    Traco("3. Contar quantidade de estados")
    Traco("4. Sair")


    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        estado = input("Digite o estado: ")
        total_orgaos = filtrar_orgaos_por_estado(estado)
        print(f"Total de órgãos no estado {estado}: {total_orgaos}")
    elif opcao == "2":
        estado = input("Digite o estado: ")
        orgaos = listar_orgaos_por_estado(estado)
        print(f"Órgãos no estado {estado}:")
        for orgao in orgaos:
            print(orgao)
    elif opcao == "3":
        total_estados = contar_estados_no_arquivo()
        print(f"Quantidade de estados no arquivo: {total_estados}")
    elif opcao == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
