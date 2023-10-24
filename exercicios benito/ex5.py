valor = int(input("Entre com um númrero, para saber o quadrado perfeito:"))
aux = 1

raizQuad = int(valor ** (1/2))


if ((raizQuad ** 2 )== valor):
    print("O número {0} é um quadrado perfeito!".format(int(valor)))
else:
    print("O número {0} não é um quadrado perfeito!".format(int(valor)))


print("Os dez primeiros quadrado perfeito: ")
while(aux<= 10):
    print("{0} ^ {1} = {2}".format(aux, 2, (aux ** 2)))
    aux += 1