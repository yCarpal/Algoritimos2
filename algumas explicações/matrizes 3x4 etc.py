
matriz = []
for l in range(3):
    # Crie uma lista vazia para cada linha
    linha = []
    
    # Preencha a linha com os elementos desejados
    for c in range(4):
        elemento = input(f"Digite o elemento da posição ({l+1}, {c+1}): ")
        linha.append(elemento)
    
    # Adicione a linha à matriz principal
    matriz.append(linha)