
def encontra_impares(lista):
    lista1 = []
    if len(lista) >= 1:
        if lista[0] % 2 != 0:
            lista1.append(lista[0])
        lista1 = lista1 + encontra_impares(lista[1:])
    return lista1
