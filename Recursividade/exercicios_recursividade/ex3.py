# Construa uma função que receba como parâmetro uma matriz quadrada 4 X 4 e retorne a soma dos valores da diagonal principal.
def Somaprinc(S):
    print(sum(diagonal))
    return diagonal


Matriz = [[9,2,3,8],
          [1,8,7,4],
          [1,6,3,4],
          [5,2,3,4]]

diagonal = [Matriz[l][l] for l in range(4)]


print('A Matriz é:')
for linha in Matriz:
    print(linha)

print('A Diagonal da Matriz é:')
print(diagonal)
print("A soma da diagonal principal é: ")
print(Somaprinc(diagonal))