aqua = open('trabalgo/aquaviarios.csv', 'r')
for linha in aqua:
    colunas = linha.split(',')
    print((colunas[3]))