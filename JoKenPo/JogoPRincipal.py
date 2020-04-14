import JoKenPo.Uteis.textos
import JoKenPo.Uteis.NPCS
import JoKenPo.Uteis.Funções
import JoKenPo.Uteis.Audios
from time import sleep
import playsound
vidas = 1
result = 0
#Programa Principal
JoKenPo.Uteis.textos.fala('Esse é um jogo em homenagem ao querido personagem da SEGA, Alex Kidd, dedicado aos saudosos \n'
      '               e apaixonados players dos sistemas 8 e 16 bit.')
sleep(2)
JoKenPo.Uteis.textos.telaini()
sleep(2)
player = str(input('Qual o seu nome? ')).capitalize()


while vidas > 0:
    #Enfrentando o Alex Kidd
    while result == 0:
        lista = JoKenPo.Uteis.NPCS.alex(player, result, vidas)
        result = lista[1]
        vidas = lista[2]
        if vidas == 0:
            JoKenPo.Uteis.Funções.gameover()
        if result == 1:
            JoKenPo.Uteis.Audios.passafase()
            # Enfrentando o Cabeça de pedra
            result = 0
            while result == 0:
                lista = JoKenPo.Uteis.NPCS.stone(player, result, vidas)
                result = lista[1]
                vidas = lista[2]
                if vidas == 0:
                    JoKenPo.Uteis.Funções.gameover()
                if result == 1:
                    JoKenPo.Uteis.Audios.passafase()
                    # Enfrentando o Cabeça de tesoura
                    result = 0
                    while result == 0:
                        lista = JoKenPo.Uteis.NPCS.scizor(player, result, vidas)
                        result = lista[1]
                        vidas = lista[2]
                        if vidas == 0:
                            JoKenPo.Uteis.Funções.gameover()
                        if result == 1:
                            JoKenPo.Uteis.Audios.passafase()
                            # Enfrentando o Cabeça de papel
                            result = 0
                            while result == 0:
                                lista = JoKenPo.Uteis.NPCS.paper(player, result, vidas)
                                result = lista[1]
                                vidas = lista[2]
                                if vidas == 0:
                                    JoKenPo.Uteis.Funções.gameover()
                                if result == 1:
                                    JoKenPo.Uteis.Audios.passafase()
                                    # Enfrentando o Grande Janken
                                    result = 0
                                    while result == 0:
                                        lista = JoKenPo.Uteis.NPCS.janken(player, result, vidas)
                                        result = lista[1]
                                        vidas = lista[2]
                                        if vidas == 0:
                                            JoKenPo.Uteis.Funções.gameover()
