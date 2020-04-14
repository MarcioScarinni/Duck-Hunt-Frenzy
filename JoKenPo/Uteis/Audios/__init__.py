import simpleaudio as sa


def morre():
    filename = 'AudiosJoken\Perde.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def ganha():
    filename = 'AudiosJoken\Ganha.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def passafase():
    filename = 'AudiosJoken\PassaFAse.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()