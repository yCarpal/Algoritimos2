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
        indice_coluna = cabecalho.index("CD_CATEGORIA")

        # Percorre as linhas do arquivo, adicionando os valores únicos ao conjunto
        for linha in linhas[1:]:
            valores_unicos.append(linha.strip().split(',')[indice_coluna])

    # Mostra os valores únicos da coluna
    for valor in valores_unicos:
        print(valor)

    
def listar_orgaos_por_categoria(categoria):
    categoriass = []
    with open("trabalgo/aquaviario.csv", "r") as categorias:
        linhas = categorias.readlines()
        for i in linhas[1:]:
            campos = i.strip().split(',')
            if campos[4] == categoria:
                categoriass.append(campos[3])  # Adicione o órgão à lista
    return categoriass

while True:
    Traco("Menu de Opções:")
    Traco("1. Listar órgãos por categoria")
    Traco("2. Sair do sistema")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        mostrar_categorias()
        cat = input("Digite a categoria: \n")
        cats = listar_orgaos_por_categoria(cat)
        print(f"Órgãos na categoria {cat}:\n")
        for i in cats:
            print(i)
    elif opcao == "2":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
