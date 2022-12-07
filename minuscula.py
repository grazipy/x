def maiusculas(frase):
    maiusculas = []

    for i in range(len(frase)):
        caracter = frase[i]
        decASCII = ord(caracter)

        if decASCII > 64 and decASCII < 91:
            maiusculas.append(caracter)

    return "".join(maiusculas)

# Testa único caracter em maiúsculo
def test_unicoMaiusculo():
    assert maiusculas('Programamos em python 2?') == 'P'

# Testa vários caracteres em maiúsculo
def test_variosMaiusculos():
    assert maiusculas('PrOgRaMaMoS em python!') == 'PORMMS'
