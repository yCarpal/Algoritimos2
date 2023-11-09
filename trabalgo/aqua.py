def filtrar_distritos(aqua):
    aqua = open('trabalgo/aquaviarios.csv', 'r')  # Abra o arquivo 'trabalho/aquaviarios.csv'

    with open(aqua, 'r') as trabalgo:
        dados = trabalgo.readlines()

    # Crie um filtro para obter apenas os distritos de 1 a 9
    distritos_filtrados = [distrito.strip() for distrito in dados if 1 <= int(distrito.split(',')[0]) <= 9]

    # Itere sobre os distritos filtrados e imprima seus respectivos órgãos
    for distrito in distritos_filtrados:
        codigo, orgao = distrito.split(',')
        print(f"Distrito {codigo}: {orgao}")

filtrar_distritos('aquaviario.txt')