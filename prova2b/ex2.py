# Faça um algoritmo que armazene 25 valores em uma variável (array,
# lista, tupla ou conjunto). O algoritmo deverá armazenar em uma nova variável os
# valores na ordem inversa e com o sinal inverso. Exemplo:

N = 25
Lista = []
print("A lista original é:")
for i in range(N):
    valor = int(input("Insira valores para a lista: "))
    Lista.append(valor)
print(Lista)
print("-="*30)

print("A lista inversa será: ")
reverso = Lista[::-1]

for i in range(N):
    Lista[i] = -reverso[i]
    
print('-='*30)
print(f"O reverso da matriz é : {reverso} ja a lista com elementos negativados fica: {Lista}")

