import pygame
from random import randint

pygame.init()
pygame.mixer.init()


class Mira(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        self.Imagemmira = pygame.image.load('imagens/mira.png')
        self.rect = self.Imagemmira.get_rect()
        self.rect.top = posy - 22
        self.rect.left = posx - 22
        self.tiroSom = pygame.mixer.Sound('sons/tiroduckh.ogg')
        self.atirando = False


    def mostrar(self, screen):
        screen.blit(self.Imagemmira, self.rect)
        self.rect.top = self.rect.top
        self.rect.left = self.rect.left
        pygame.mouse.set_visible(False)


    def atira(self,screen):
        if not self.atirando:
            screen.fill((255,255,255))
            self.tiroSom.play()
            self.atirando = True
        else:
            self.atirando = False


class Pato(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sompato = pygame.mixer.Sound('sons/pato.ogg')
        self.sompato.play()
        self.images = [pygame.image.load('imagens/pato.png'),
                        pygame.image.load('imagens/pato3.png'),
                       pygame.image.load('imagens/pato2.png'),
                       pygame.image.load('imagens/patocai.png'),
                        pygame.image.load('imagens/patocai2.png')]
        self.current_image = 0
        self.image = pygame.image.load('imagens/pato.png')
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.tocando = False
        self.passou = True


    def update(self, ti):
        self.current_image = (self.current_image + 1) % 3
        if self.passou:
            if self.rect.left >= -170:
                self.passou = True
                self.rect.left += 50
                self.image = self.images[self.current_image]

                if self.rect.left >= 900:
                    self.passou = False
        else:
            if self.rect.left <= 900:
                self.passou = False
                self.rect.left -= 50
                self.image = self.images[self.current_image]
                self.image = pygame.transform.flip(self.image, True, False)
                if self.rect.left <= -160:
                    self.passou = True




    def cai(self, screen):
        if not self.tocando:
            self.sompato = pygame.mixer.Sound('sons/patocaindo.ogg')
            self.sompato.play()
            self.tocando = True
        self.images = [pygame.image.load('imagens/patocai.png'),
                       pygame.image.load('imagens/patocai3.png'),
                       pygame.image.load('imagens/patocai2.png'),
                       pygame.image.load('imagens/patocai4.png')]
        self.current_image = (self.current_image + 1) % 4
        self.image = self.images[self.current_image]
        self.rect.top += 11
        screen.blit(self.image, (self.rect.left, self.rect.top))


def is_offscreen(sprite):
    if sprite.rect[0] > 900 or sprite.rect[0] < -160:
        return True