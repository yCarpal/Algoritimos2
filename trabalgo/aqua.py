def contar_orgaos_do_distrito(distrito):
    contador = 0
    with open("trabalgo/aquaviario.csv", "r") as arquivo:
        linhas = arquivo.readlines()
        for i in linhas[1:]:  # Ignora o cabeçalho (primeira linha)
            campos = i.strip().split(',')
            if campos[0] == distrito:
                contador += 1
    return contador

def listar_orgaos_do_distrito(distrito):
    with open("trabalgo/aquaviario.csv", "r") as arquivo:
        linhas = arquivo.readlines()
        for i in linhas[1:]:  # Ignora o cabeçalho (primeira linha)
            campos = i.strip().split(',')
            if campos[0] == distrito:
                print(f'Distrito {distrito}: {campos[1]}, {campos[2]}')

# Código principal
# Lendo o número do distrito do usuário
distrito = input('Digite o número do distrito (de 1 a 9) para listar os órgãos do aquaviário: ')

# Verificando se o número do distrito é válido
if distrito not in map(str, range(1, 10)): # map ele é usado para criar um iterável com os números de 1 a 9 como strings e, em seguida, verifica se o valor inserido pelo usuário está contido nesse iterável.
    print('Número de distrito inválido')
else:
    listar_orgaos_do_distrito(distrito)
