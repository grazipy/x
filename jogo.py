def computador_escolhe_jogada(n, m):
    c_remove = 1
    while c_remove != m:
        if (n - c_remove) % (m+1) == 0:
            return c_remove
        else:
            c_remove += 1
    return c_remove


def usuario_escolhe_jogada(n, m):
    jogada_val = True
    while jogada_val:
        j_remove = int(input('Quantas peças você vai tirar? '))
        if j_remove > m or j_remove < 1:
            print('\nOops! Jogada inválida! Tente de novo.\n')
        else:
            jogada_val = False
    return j_remove


def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    c_vez = False
    if n % (m+1) == 0:
        print('\nVoce começa!\n')
    else:
        print('\nComputador começa!')
        c_vez = True
    while n > 0:
        if c_vez:
            c_remove = computador_escolhe_jogada(n, m)
            n = n - c_remove
            if c_remove == 1:
                print('\nO computador tirou uma peça.')
            else:
                print('\nO computador tirou', c_remove, 'peças.')
            c_vez = False
        else:
            j_remove = usuario_escolhe_jogada(n, m)
            n = n - j_remove
            if j_remove == 1:
                print('\nVocê tirou uma peça.')
            else:
                print('\nVocê tirou', j_remove, 'peças.')
            c_vez = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
        else:
            if n != 0:
                print('Agora restam', n, 'peças no tabuleiro.\n')
    print('Fim do jogo! O computador ganhou!')


def campeonato():
    rodada = 1
    while rodada <= 3:
        print('\n**** Rodada', rodada, '****\n')
        partida()
        rodada += 1
    print('\n**** Final do campeonato! ****')
    print('\nPlacar: Você 0 X 3 Computador')


# Início do jogo do NIM:


print('Bem-vindo ao jogo do NIM! Escolha:\n')

e = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato '))

if e == 1:
    print()
    partida()
else:
    print('\nVoce escolheu um campeonato!')
    campeonato()
