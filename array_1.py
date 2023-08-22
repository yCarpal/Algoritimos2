import numpy as np

N = 10

vetor = np.zeros(10)

for i in range(N):
    vetor[i] = float(input(f'Informe um valor para V[{i}]:'))
# mostra os valores armazenados na estrutura
media= vetor.mean()
print(vetor)
print(f"A media de todos valores armazenados no vetor é de {media}")