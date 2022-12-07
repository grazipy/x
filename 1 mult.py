def dimensoes(matriz):
    return (len(matriz), len(matriz[0]))

# Realiza a soma entre duas matrizes com mesmas dimensões
def soma_matrizes(matriz1, matriz2):
    # calcula as dimensões das matrizes recebidas
    dimensaoMatriz1 = dimensoes(matriz1)
    dimensaoMatriz2 = dimensoes(matriz2)

    # certifica que ambas possuem as mesmas dimensões
    if dimensaoMatriz1 == dimensaoMatriz2:
        matrizSoma = []

        # percorre as linhas
        for i in range(len(matriz1)):
            linha = []

            # percorre as colunas
            for j in range(len(matriz1[0])):

                # realiza a soma das matrizes e atribui os valores na linha
                soma = matriz1[i][j] + matriz2[i][j]
                linha.append(soma)

            # inclui a linha resultante na nova matriz
            matrizSoma.append(linha)

        return matrizSoma
    else:
        return False
