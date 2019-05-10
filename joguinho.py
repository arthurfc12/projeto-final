import pygame
import time
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

# Dados gerais do jogo.
WIDTH = 480 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

#Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


#Gravidade
GRAV = -5


class Player1(pygame.sprite.Sprite):
    
    
    def __init__(self, player_img):
        
         # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (50, 38))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        
        # Velocidade da nave
        self.speedx = 0
        
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 25
        
        def update(self):
            self.rect.x += self.speedx
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
                
            self.speedy -= GRAV
            self.recty += self.speedy
            

class Player2(pygame.sprite.Sprite):
    
    
    def __init__(self, player_img2):
        
         # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        self.image = player_img2
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img2, (50, 38))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        
        # Velocidade da nave
        self.speedx = 0
        
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 25
        
        def update(self):
            self.rect.x += self.speedx
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
                
            self.speedy -= GRAV
            self.recty += self.speedy
        

                


def game_screen(screen):            
        
        
        
        
# Inicialização do Pygame.

pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()
        
        
        
        
        
        
        
        
        