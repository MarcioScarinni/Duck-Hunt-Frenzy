import pygame

class Status():

    def tentativas(msg, screen):
        font = pygame.font.SysFont(None, 25, italic=True)
        texto1 = font.render(msg, True, (255,255,255))
        screen.blit(texto1, [30, 20])

    def recarregar(msg, screen):
        font = pygame.font.SysFont(None, 50, italic=True)
        texto1 = font.render(msg, True, (255, 0, 0))
        screen.blit(texto1, [150, 150])


    def timer(msg, screen):
        font = pygame.font.SysFont(None, 25, italic=True)
        texto1 = font.render(msg, True, (255,255,255))
        screen.blit(texto1, [350, 20])


    def score(msg, screen):
        font = pygame.font.SysFont(None, 25, italic=True)
        texto1 = font.render(msg, True, (255,255,255))
        screen.blit(texto1, [600, 20])


    def Gover(msg, screen):
        tocando = False
        font = pygame.font.SysFont(None, 100, italic=True)
        texto1 = font.render(msg, True, (255, 0, 0))
        screen.blit(texto1, [200, 150])
        pygame.mouse.set_visible(True)



    def hscore1(msg, screen):
        font = pygame.font.SysFont(None, 30, italic=True)
        texto1 = font.render(msg, True, (0, 0, 0))
        screen.blit(texto1, [200, 230])


    def hscore2(msg, screen):
        font = pygame.font.SysFont(None, 40, italic=True)
        texto1 = font.render(msg, True, (0, 0, 0))
        screen.blit(texto1, [300, 560])


    def hscoreSombra(msg, screen):
        font = pygame.font.SysFont(None, 45, italic=True)
        texto1 = font.render(msg, True, (255, 255, 255))
        screen.blit(texto1, [280, 560])