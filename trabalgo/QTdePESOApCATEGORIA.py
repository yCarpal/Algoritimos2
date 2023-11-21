
def Traco(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

def mostrar_categorias():
    # Nome do arquivo CSV
    nome_arquivo = 'trabalgo/aquaviario.csv'
    
    # Lista para armazenar os valores únicos da coluna desejada
    valores_unicos = []

    # Lê o arquivo CSV e extrai os valores únicos da coluna desejada
    with open(nome_arquivo, 'r') as arquivo_csv:
        linhas = arquivo_csv.readlines()
        
        # Encontra o índice da coluna
        cabecalho = linhas[0].strip().split(',')
        indice_coluna = cabecalho.index("DS_CATEGORIA_POR")

        # Percorre as linhas do arquivo, adicionando os valores únicos ao conjunto
        for linha in linhas[1:]:
            valores_unicos.append(linha.strip().split(',')[indice_coluna])

    # Mostra os valores únicos da coluna
    for valor in valores_unicos:
        print(valor)
def contar_pessoas_por_cargo(cargo):
    contador = 0
    with open("trabalgo/aquaviario.csv", "r") as cargos:
        linhas = cargos.readlines()
        for i in linhas[1:]:
            campos = i.strip().split(',')
            if campos[1] == cargo:
                contador += 1
    return contador

while True:
    Traco("Menu de Opções:")
    Traco("1. Mostrar quantidade de pessoas por cargo")  
    Traco("2. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_categorias()
        cargo = input("Digite o cargo: ")
        total_pessoas = contar_pessoas_por_cargo(cargo)
        print(f"Quantidade de pessoas que atuam no cargo '{cargo}': {total_pessoas}")
    elif opcao == "2":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")



