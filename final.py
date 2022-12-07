import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +
                      " (aperte enter para sair): ")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    s_ab = 0

    for i in range(0, 6):
        valor = as_a[i] - as_b[i]

        if valor < 0:
            valor = abs(valor)

        s_ab += valor

    return s_ab / 6


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_de_palavras = separa_palavras(texto)
    n_total_palavras = len(lista_de_palavras)

    tamanho_palavras = 0
    for i in range(n_total_palavras):
        tamanho_palavras = tamanho_palavras + len(lista_de_palavras[i])

    tamanho_medio_palavra = tamanho_palavras/n_total_palavras

    type_token = n_palavras_diferentes(texto)/n_total_palavras

    hapax_legomana = n_palavras_unicas(texto)/n_total_palavras

    n_total_sentencas = len(separa_sentencas(texto))

    n_total_frases = len(separa_frases(texto))

    tamanho_medio_sentenca = tamanho_palavras/n_total_sentencas

    complexidade_sentenca = n_total_frases/n_total_sentencas

    tamanho_medio_frase = tamanho_palavras/n_total_frases

    assinatura = [tamanho_medio_palavra, type_token, hapax_legomana,
                  tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]

    return assinatura


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    assinat = []

    for texto in textos:
        assinat.append(calcula_assinatura(texto))

    grau_similaridade = 1000.0
    texto_infectado = -1

    for i in range(0, len(assinat)):

        similaridade = compara_assinatura(ass_cp, assinat[i])

        if (similaridade < grau_similaridade):
            grau_similaridade = similaridade
            texto_infectado = i + 1

    print("O autor do texto", texto_infectado, "está infectado com COH-PIAH")
    return texto_infectado


if __name__ == "__main__":
    assinatura_cp = le_assinatura()
    textos_lidos = le_textos()
    avalia_textos(textos_lidos, assinatura_cp)
