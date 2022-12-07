def imprime_matriz(matriz):
    for linha in matriz:
        for index, coluna in enumerate(linha):
            if index == (len(matriz[0]) - 1):
                print(coluna, end="")
            else:
                print(coluna, end=" ")
        print("")
