import JoKenPo.Uteis.textos
from time import sleep
import JoKenPo.Uteis.Audios



def alex(p, r, v):
    placar = ''
    perde = ganha = 0
    JoKenPo.Uteis.textos.fala(f'Olá {p}, me chamo Alex, sou o Príncipe de Radaxian e te lanço '
        f'um desafio pra uma partida de Jo Ken Po! Vamos ver se é capaz de me vencer!')
    while perde < 2 and ganha < 2:
        JoKenPo.Uteis.textos.linha()
        print(f'Placar: ', end='')
        for i in placar:
            print(f'\033[7m{i}\033[m', end='')
        print(f'{p:>78} = {v}')
        choice = (input(
            'Escolha entre \033[31mPEDRA\033[m - \033[31mPAPEL\033[m ou \033[31mTESOURA\033[m: \n').strip().upper())
        if choice == "PEDRA":
            placar += (JoKenPo.Uteis.Funções.jokenpo(choice))
        elif choice == 'PAPEL':
            placar += (JoKenPo.Uteis.Funções.jokenpo(choice))
        elif choice == 'TESOURA':
            placar += (JoKenPo.Uteis.Funções.jokenpo(choice))
        else:
            print('\033[31mEscolha inválida\033[m')
            sleep(1)
        perde = placar.count('X')
        ganha = placar.count('O')
    print(f'Placar: ', end='')
    for i in placar:
        print(f'\033[7m{i}\033[m', end='')
    print('')
    if perde == 2:
        JoKenPo.Uteis.textos.fala('Você perdeu!')
        v -= 1
        r = 0
        JoKenPo.Uteis.Audios.morre()
        return (p, r, v)
    if ganha == 2:
        JoKenPo.Uteis.textos.fala('Parabéns, você me venceu! Provou ser capaz de me representar nessa jornada!')
        sleep(0.5)
        JoKenPo.Uteis.textos.fala('Você precisa derrotar o \033[31mCabeça de Pedra\033[m, o \033[31mCabeça de Tesoura\033[m e o \033[31mCabeça de Papel\033[m!')
        sleep(0.5)
        JoKenPo.Uteis.textos.fala('E finalmente o \033[31mGrande Janken\033[m!')
        sleep(0.5)
        JoKenPo.Uteis.textos.fala('Só assim poderá salvar Radaxian do grande mal que a assola!')
        sleep(0.5)
        JoKenPo.Uteis.textos.fala('Vá. pegue essa \033[36mVIDA EXTRA\033[m e vá para o Miracle World procurar respostas !')
        r = 1
        v += 1
        return (p, r, v)


def stone(p, r, v):
    placar = ''
    perde = ganha = 0
    JoKenPo.Uteis.textos.fala(
        f'Hahaha! Finalmente te encontrei, \033[31m{p}\033[m, sou o \033[31mGooseka\033[m, o \033[31mCabeça de Pedra\033[m, primeiro capanga do '
        f'Grande Janken! \nJo Ken Po! Vamos ver se é capaz de me vencer!')
    while perde < 2 and ganha < 2:
        JoKenPo.Uteis.textos.linha()
        print(f'Placar: ', end='')
        for i in placar:
            print(f'\033[7m{i}\033[m', end='')
        print(f'{p:>78} = {v}')
        choice = (input(
            'Escolha entre \033[31mPEDRA\033[m - \033[31mPAPEL\033[m ou \033[31mTESOURA\033[m: \n').strip().upper())
        if choice == "PEDRA":
            placar += (JoKenPo.Uteis.Funções.jokenpo(choice))
        elif choice == 'PAPEL':
            placar += (JoKenPo.Uteis.Funções.jokenpo(choice))
        elif choice == 'TESOURA':
            placar += (JoKenPo.Uteis.Funções.jokenpo(choice))
        else:
            print('\033[31mEscolha inválida\033[m')
            sleep(1)
        perde = placar.count('X')
        ganha = placar.count('O')
    print(f'Placar: ', end='')
    for i in placar:
        print(f'\033[7m{i}\033[m', end='')
    print('')
    if perde == 2:
        JoKenPo.Uteis.textos.fala('Você perdeu!')
        v -= 1
        r = 0
        JoKenPo.Uteis.Audios.morre()
        return (p, r, v)
    if ganha == 2:
        JoKenPo.Uteis.textos.fala('Nããããããoooooo.')
        sleep(0.5)
        JoKenPo.Uteis.textos.fala('O \033[31mGrande JANKEN\033[m vai me matar!')
        sleep(0.5)
        JoKenPo.Uteis.textos.fala('Você precisa me ajudar, destrua ele antes que ele me destrua! Tome aqui essa vida extra!')
        sleep(0.5)
        JoKenPo.Uteis.textos.fala('\033[36mVocê ganhou uma tentativa extra!\033[m')
        v += 1
        r = 1
        JoKenPo.Uteis.Audios.ganha()
        return (p, r, v)


def scizor(p, r, v):
    placar = ''
    perde = ganha = 0
    JoKenPo.Uteis.textos.fala(
        f'Hahaha! Ora, ora... \033[31m{p}\033[m em pessoa, sou o \033[31mChokkina\033[m, '
        f'também conhecido como o \033[31mCabeça de Pedra\033[m, segundo capanga do '
        f'\033[31mGrande Janken\033[m! \nGaranto que daqui você não passa!')
    while perde < 2 and ganha < 2:
        JoKenPo.Uteis.textos.linha()
        print(f'Placar: ', end='')
        for i in placar:
            print(f'\033[7m{i}\033[m', end='')
        print(f'{p:>78} = {v}')
        choice = (input(
            'Escolha entre \033[31mPEDRA\033[m - \033[31mPAPEL\033[m ou \033[31mTESOURA\033[m: \n').strip().upper())
        if choice == "PEDRA":
            placar += (JoKenPo.Uteis.Funções.jokenpo(choice))
        elif choice == 'PAPEL':
            placar += (JoKenPo.Uteis.Funções.jokenpo(choice))
        elif choice == 'TESOURA':
            placar += (JoKenPo.Uteis.Funções.jokenpo(choice))
        else:
            print('\033[31mEscolha inválida\033[m')
            sleep(1)
        perde = placar.count('X')
        ganha = placar.count('O')
    print(f'Placar: ', end='')
    for i in placar:
        print(f'\033[7m{i}\033[m', end='')
    print('')
    if perde == 2:
        JoKenPo.Uteis.textos.fala('Você perdeu!')
        v -= 1
        r = 0
        JoKenPo.Uteis.Audios.morre()
        return (p, r, v)
    if ganha == 2:
        JoKenPo.Uteis.textos.fala('O quêêê!?.')
        sleep(0.5)
        JoKenPo.Uteis.textos.fala('Eu não acredito que perdi pra você!')
        sleep(0.5)
        JoKenPo.Uteis.textos.fala(
            'Vou fugir daqui... Mas tenho certeza que meu chefe, o \033[31mCabeça de Papel\033[m, vai dar cabo de você')
        sleep(0.5)
        JoKenPo.Uteis.textos.fala('\033[36mAo fugir, ele deixa cair uma vida extra!\033[m')
        v += 1
        r = 1
        JoKenPo.Uteis.Audios.ganha()
        return (p, r, v)


def paper(p, r, v):
    placar = ''
    perde = ganha = 0
    JoKenPo.Uteis.textos.fala(
        f'O queee?! Aqueles incompetentes não te detiveram? Sou o \033[31mParplin\033[m, '
        f'o temido \033[31mCabeça de Papel\033[m, terceiro capanga do '
        f'\033[31mGrande Janken\033[m! \nVou exterminar você!')
    while perde < 2 and ganha < 2:
        JoKenPo.Uteis.textos.linha()
        print(f'Placar: ', end='')
        for i in placar:
            print(f'\033[7m{i}\033[m', end='')
        print(f'{p:>78} = {v}')
        choice = (input(
            'Escolha entre \033[31mPEDRA\033[m - \033[31mPAPEL\033[m ou \033[31mTESOURA\033[m: \n').strip().upper())
        if choice == "PEDRA":
            placar += (JoKenPo.Uteis.Funções.jokenpo(choice))
        elif choice == 'PAPEL':
            placar += (JoKenPo.Uteis.Funções.jokenpo(choice))
        elif choice == 'TESOURA':
            placar += (JoKenPo.Uteis.Funções.jokenpo(choice))
        else:
            print('\033[31mEscolha inválida\033[m')
            sleep(1)
        perde = placar.count('X')
        ganha = placar.count('O')
    print(f'Placar: ', end='')
    for i in placar:
        print(f'\033[7m{i}\033[m', end='')
    print('')
    if perde == 2:
        JoKenPo.Uteis.textos.fala('Você perdeu!')
        v -= 1
        r = 0
        JoKenPo.Uteis.Audios.morre()
        return (p, r, v)
    if ganha == 2:
        JoKenPo.Uteis.textos.fala('Impossível!!!!!!')
        sleep(0.5)
        JoKenPo.Uteis.textos.fala('Você trapaceou! Eu sou o segundo melhor do mundo no Jo Ken Po!')
        sleep(0.5)
        JoKenPo.Uteis.textos.fala(
            'Mas agora você vai ser destruído! Meu grande mestre, o \033[31mGrande Janken\033[m não te deixará impune!')
        sleep(0.5)
        JoKenPo.Uteis.Audios.ganha()
        JoKenPo.Uteis.textos.fala('\033[31mParplin\033[m some numa nuvem de fumaça!')
        r = 1
        return (p, r, v)


def janken(p, r, v):
    placar = ''
    perde = ganha = 0
    JoKenPo.Uteis.textos.fala(
        f'Quem ousa interromper o \033[31mGrande Janken\033[m? '
        f'Vou esmagar você como um inseto que você é, \033[31m{p}\033[m!')
    while perde < 2 and ganha < 2:
        JoKenPo.Uteis.textos.linha()
        print(f'Placar: ', end='')
        for i in placar:
            print(f'\033[7m{i}\033[m', end='')
        print(f'{p:>78} = {v}')
        choice = (input(
            'Escolha entre \033[31mPEDRA\033[m - \033[31mPAPEL\033[m ou \033[31mTESOURA\033[m: \n').strip().upper())
        if choice == "PEDRA":
            placar += (JoKenPo.Uteis.Funções.jokenpo(choice))
        elif choice == 'PAPEL':
            placar += (JoKenPo.Uteis.Funções.jokenpo(choice))
        elif choice == 'TESOURA':
            placar += (JoKenPo.Uteis.Funções.jokenpo(choice))
        else:
            print('\033[31mEscolha inválida\033[m')
            sleep(1)
        perde = placar.count('X')
        ganha = placar.count('O')
    print(f'Placar: ', end='')
    for i in placar:
        print(f'\033[7m{i}\033[m', end='')
    print('')
    if perde == 2:
        JoKenPo.Uteis.textos.fala('Você perdeu!')
        v -= 1
        r = 0
        JoKenPo.Uteis.Audios.morre()
        return (p, r, v)
    if ganha == 2:
        JoKenPo.Uteis.textos.fala('NÃO PODE SER!')
        sleep(0.5)
        JoKenPo.Uteis.textos.fala('Eu perdi pra esse INSETO!')
        sleep(0.5)
        JoKenPo.Uteis.textos.fala(f'Que vergonha, ser derrotado no Jo Ken Po por esse, esse tal... \033[31m{p}\033[m !')
        sleep(0.5)
        JoKenPo.Uteis.textos.fala(f'\033[31mJanken\033[m se curva diante do\033[31m Grande {p}\033[m. O novo MESTRE DO JO KEN PO!')
        r = 1
        JoKenPo.Uteis.Audios.ganha()
        return (p, r, v)