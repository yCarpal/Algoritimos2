tamanho = 3
largura = 3
matriz = []

# Preencher a matriz
 
 
# Calcular a média da diagonal
diagonal = [matriz[l][l] for l in range(min(tamanho, largura))]
media_diagonal = sum(diagonal) / len(diagonal)

print('A Matriz é:')
for linha in matriz:
    print(linha)

print('A Diagonal da Matriz é:')
print(diagonal)
print('A Média dos valores da diagonal é:')
print(media_diagonal)