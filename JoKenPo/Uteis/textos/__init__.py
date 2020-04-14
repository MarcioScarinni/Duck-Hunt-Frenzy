from time import sleep
import simpleaudio as sa


def linha():
    print('=-='*30)


def telaini():
    filename = 'AudiosJoken\Intro.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    text = "Alex Kidd's - Jo Ken Po"
    print('\033[36m~' * 90)
    print('=' * 90)
    print(f'{"=":<35}', end='\033[m')
    for i in text:
        print(f'\033[33m{i}', end='')
        sleep(0.3)
    print(f'\033[36m {"=":>31}')
    print('=' * 90)
    print('~' * 90, '\033[m')


def fala(txt):
    filename = 'AudiosJoken\Escreve.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    for i in txt:
        print(i, end='')
        sleep(0.01)
    print('')
    play_obj.stop()
    #pygame.mixer.music.stop()


def quadro(txt):
    print('\033[33m~' * (len(txt)+4))
    print('=' * (len(txt)+4))
    print('= ', end='\033[m')
    for i in txt:
        print(f'\033[35m{i}', end='')
        sleep(0.01)
    print('\033[33m =')
    print('=' * (len(txt) + 4))
    print('~' * (len(txt) + 4), '\033[m')


def pensando():
    filename = 'AudiosJoken\Musica.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    print('Pensando', end='')
    p = '.' * 10
    for i in p:
        print(i, end=' ')
        sleep(1)
    print('')


def jankaudio():
    print('JO')
    filename = 'AudiosJoken\Jo.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    print('KEN')
    filename = 'AudiosJoken\Ken.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    print('PO')
    filename = 'AudiosJoken\Po.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
