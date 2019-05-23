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
GRAV = 5
#Tamanho do pulo
JUMP_SIZE = 30
#Altura do chão
GROUND = HEIGHT * 5 // 6


#Estados do jogador
STILL = 0
JUMPING = 1
FALLING = 2

class Player1(pygame.sprite.Sprite):
    
    
    def __init__(self, player_img):
        
         # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        #Estado do jogador
        self.state = STILL
        
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
        
        # Velocidade do jogador
        self.speedx = 0
        
        #velocidade em y
        self.speedy = 0
        
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 25
        
    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
                            
            
        self.speedy += GRAV
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
            self.rect.y += self.speedy
            # Se bater no chão, para de cair
            if self.rect.bottom > GROUND:
                # Reposiciona para a posição do chão
                self.rect.bottom = GROUND
                # Para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
                
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING
                
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
        

                
def load_assets(img_dir, snd_dir):
    assets = {}
    assets["background"] =  pygame.image.load(path.join(img_dir, 'Background.png')).convert()

def game_screen(screen):
    #carrega assets
    assets = load_assets(img_dir, snd_dir)
    
    background = assets["background"]
    background_rect = background.get_rect()
            
        
        
        
        
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
        
        
        
        
        
        
        
        
        