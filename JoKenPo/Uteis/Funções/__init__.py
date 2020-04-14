opções = ['PEDRA', 'PAPEL', 'TESOURA']
from random import choice
import pygame
import JoKenPo.Uteis.textos
from time import sleep
import simpleaudio as sa


def jokenpo(pl):
    inimigo = choice(opções)
    if inimigo == 'PEDRA':
        JoKenPo.Uteis.textos.pensando()
        JoKenPo.Uteis.textos.jankaudio()
        if pl == 'TESOURA':
            JoKenPo.Uteis.textos.linha()
            JoKenPo.Uteis.textos.fala(f'Eu escolhi \033[31m{inimigo}\033[m')
            JoKenPo.Uteis.textos.fala('\033[31mVocê perdeu. Eu ganhei!\033[m')
            return 'X'
        elif pl == 'PAPEL':
            JoKenPo.Uteis.textos.linha()
            JoKenPo.Uteis.textos.fala(f'Eu escolhi \033[31m{inimigo}\033[m')
            JoKenPo.Uteis.textos.fala('\033[34mVocê ganhou. Eu perdi!\033[m')
            return 'O'
        else:
            JoKenPo.Uteis.textos.linha()
            JoKenPo.Uteis.textos.fala(f'Eu também escolhi \033[31m{inimigo}\033[m')
            JoKenPo.Uteis.textos.fala('\033[33mEmpatamos!\033[m!')
            return ''
    if inimigo == 'TESOURA':
        JoKenPo.Uteis.textos.pensando()
        JoKenPo.Uteis.textos.jankaudio()
        if pl == 'PAPEL':
            JoKenPo.Uteis.textos.linha()
            JoKenPo.Uteis.textos.fala(f'Eu escolhi \033[31m{inimigo}\033[m')
            JoKenPo.Uteis.textos.fala('\033[31mVocê perdeu. Eu ganhei!\033[m')
            return 'X'
        elif pl == 'PEDRA':
            JoKenPo.Uteis.textos.linha()
            JoKenPo.Uteis.textos.fala(f'Eu escolhi \033[31m{inimigo}\033[m')
            JoKenPo.Uteis.textos.fala('\033[34mVocê ganhou. Eu perdi!\033[m')
            return 'O'
        else:
            JoKenPo.Uteis.textos.linha()
            JoKenPo.Uteis.textos.fala(f'Eu também escolhi \033[31m{inimigo}\033[m')
            JoKenPo.Uteis.textos.fala('\033[33mEmpatamos!\033[m!')
            return ''
    if inimigo == 'PAPEL':
        JoKenPo.Uteis.textos.pensando()
        JoKenPo.Uteis.textos.jankaudio()
        if pl == 'PEDRA':
            JoKenPo.Uteis.textos.linha()
            JoKenPo.Uteis.textos.fala(f'Eu escolhi \033[31m{inimigo}\033[m')
            JoKenPo.Uteis.textos.fala('\033[31mVocê perdeu. Eu ganhei!\033[m')
            return 'X'
        elif pl == 'TESOURA':
            JoKenPo.Uteis.textos.linha()
            JoKenPo.Uteis.textos.fala(f'Eu escolhi \033[31m{inimigo}\033[m')
            JoKenPo.Uteis.textos.fala('\033[34mVocê ganhou. Eu perdi!\033[m')
            return 'O'
        else:
            JoKenPo.Uteis.textos.linha()
            JoKenPo.Uteis.textos.fala(f'Eu também escolhi \033[31m{inimigo}\033[m')
            JoKenPo.Uteis.textos.fala('\033[33mEmpatamos!\033[m')
            return ''


def gameover():
    filename = 'AudiosJoken\GameOver.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    txt = 'Game Over'
    print('\033[33m~' * 90)
    print('=' * 90)
    print(f'{"=":<40}', end='\033[m')
    for i in txt:
        print(f'\033[31m{i}', end='')
        sleep(0.4)
    print(f'\033[33m {"=":>40}')
    print('=' * 90)
    print('~' * 90, '\033[m')
    exit()
