#1.Faça uma sub-rotina que recebe duas listas A e B com dez
#elementos inteiros como parâmetro. A sub-rotina deverá determinar
#e mostrar o vetor C que contém os elementos que estão em A, mas
#que não estão em B. A lista C deverá ser mostrada no programa
#principal.


V1 = [1,2,3,4,5,6,7,8,9,0]
V2 = [3,2,6,10,5,12,13,6,1,80]
V3 = []


def encontra(a: list, b: list, c:list):
    """
    Preenche a lista c com os elemetos de a que não 
    estão em b
    """
    for i in a:
        if i not in b:
            c.append(i)

encontra( V1, V2, V3)
print(V3)




