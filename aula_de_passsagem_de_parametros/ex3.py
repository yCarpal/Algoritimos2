def substitui(v:list):
    """Recebe uma lista de inteiros e substitui
      seus valores negativos por zero"""

    for i in range(len(v)):
        if v[i] < 0:
            v[i] = 0


vetor =[1,-2,3,4, -5,6,7,8,-9,10,-11,-12, 13,14,15,-16,17,-18,19,20,21,22,23,24,25]

substitui(vetor)

print(vetor)
