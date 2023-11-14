def filtrar_e_contar_orgaos_por_estado(arquivo):
    orgaos_por_estado = {}  # Dicionário para armazenar órgãos por estado

    with open(arquivo, "r") as estados:
        linhas = estados.readlines()
        for i in linhas[1:]:  # Ignora a primeira linha
            campos = i.strip().split(',')
            estado = campos[0]
            orgao = campos[1]

            # Adicione o órgão ao estado correspondente
            if estado not in orgaos_por_estado:
                orgaos_por_estado[estado] = []
            orgaos_por_estado[estado].append(orgao)

    # Mostrar a quantidade de estados e órgãos
    total_estados = len(orgaos_por_estado)
    print(f"Total de estados: {total_estados}")

    for estado, orgaos in orgaos_por_estado.items():
        print(f"Estado: {estado} - Total de órgãos: {len(orgaos)}")
        print("Órgãos:")
        for orgao in orgaos:
            print(f"  {orgao}")

def menu():
    print("Menu de Opções:")
    print("1. Filtrar e contar órgãos por estado")
    print("2. Sair")

arquivo_aquaviarios = "aquaviario.csv"

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        filtrar_e_contar_orgaos_por_estado(arquivo_aquaviarios)
    elif opcao == "2":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")