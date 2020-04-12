#importações
import pygame
import os
import Duck.Objetos
import Duck.Dados
from random import choice
import Duck.Textos

#inicializações
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.mixer.init()
pygame.display.init()
pygame.display.set_caption('Duck Hunt Frenzy')

#criando o High Score
Hscore = "Dados/Hscore.txt"
if Duck.Dados.arqExiste(Hscore):
    print(f'Carregando arquivo {Hscore}')
else:
    Duck.Dados.criaArq(Hscore)
    Duck.Dados.criaNovo(Hscore, "pai", 0)
score = 0
melhorscore = 0
H = Duck.Dados.lerArq(Hscore)
print(H)

#barra superior
barrapreta = pygame.Surface((800,50))
barrapreta.fill((0,0,0))
borda1 = pygame.Surface((800,2))
borda1.fill((255,255,255))

#variáveis
TELA_LARGURA = 800
TELA_ALTURA = 600
y2 = []
x2 = (-170, 850)
for i in range(50, 400,10):
    y2.append(i)
x = choice(x2)
y = choice(y2)

BACKGROUND = pygame.image.load('imagens/cenario.png')
mato = pygame.image.load('imagens/matinho.png')
controltiro = [False, False]
tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
fps = pygame.time.Clock()

time = 0

pato_group = pygame.sprite.Group()
pato = Duck.Objetos.Pato(x, y)
pato_group.add(pato)

mira_group = pygame.sprite.Group()
mouse = pygame.mouse.get_pos()
#mira2 = Duck.Objetos.Mira(mouse[0], mouse[1])
#mira_group.add(mira2)

tiros = 2
toptexto = Duck.Textos.Status

miss = 0
vivo = True
introsfx = pygame.mixer.Sound('sons/intro.ogg')
introsfx.play()
pygame.event.wait()
goversfx = pygame.mixer.Sound('sons/gover.ogg')
gover = False
if gover:
    goversfx.play()


#Jogo Principal

while True:
    time += 1 / 10
    reg = 96 - time
    fps.tick(13)
    mouse = pygame.mouse.get_pos()
    '''mira_group.update(tela)
    mira_group.draw(tela)'''
    mira = Duck.Objetos.Mira(mouse[0], mouse[1])

    tela.blit(BACKGROUND, (0,0))
    tela.blit(barrapreta, (0,0))
    tela.blit(borda1,(0,51))

    if time >= 5.5:
        pato_group.update(time)
        pato_group.draw(tela)

    #eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                controltiro[0] = True
            if event.key == pygame.K_r and tiros == 0:
                controltiro[1] = True
                tiros = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                controltiro[0] = False
            if event.key == pygame.K_r:
                controltiro[1] = False
    if controltiro[0] and tiros == 0:
        toptexto.recarregar('Pressione R para RECARREGAR', tela)
    if controltiro[0] and tiros > 0:
        mira.atira(tela)
        tiros -= 1
        controltiro[0] = False
        if mira.rect.colliderect(pato):
            score += 10
            vivo = False
    if not vivo:
        pato.cai(tela)


    tela.blit(mato, (0, 0))
    toptexto.score(f'Pontuação: {score}', tela)
    toptexto.tentativas(f'Tiros: {tiros}', tela)

    #define o tempo de jogo
    if time >= 95.5:
        tiros = 0
        toptexto.timer(f'Tempo: 0', tela)
        toptexto.Gover('Fim de jogo', tela)
        toptexto.hscore1(f'Melhor pontuação: {H}', tela)
        pygame.display.update()
        gover = True
    else:

        #mira.mostrar(tela)
        if time >= 5.5:
            mira.mostrar(tela)
            toptexto.timer(f'Tempo: {reg:.0f}', tela)

        if Duck.Objetos.is_offscreen(pato_group.sprites()[0]):
            pato_group.remove(pato_group.sprites()[0])
            pato = Duck.Objetos.Pato(x, y)
            pato_group.add(pato)
            vivo = True
            y = choice(y2)
            x = choice(x2)
    # trata os highscore
    if score > H:
        melhorscore = score
        Duck.Dados.criaArq(Hscore)
        Duck.Dados.criaNovo(Hscore,"", score)
        toptexto.hscore2(f'High Score: {melhorscore}', tela)
    else:
        toptexto.hscore2(f'High Score: {H}', tela)

    pygame.display.update()
