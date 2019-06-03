# -*- coding: utf-8 -*-

#importa bibliotecas
import pygame
from os import path
import time

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

# Dados gerais do jogo.
WIDTH = 900 # Largura da tela
HEIGHT =  600 # Altura da tela
FPS = 60 # Frames por segundo
    

#Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


#Gravidade
GRAV = 3
#Tamanho do pulo
JUMP_SIZE = 35
#Altura do chão
GROUND = HEIGHT * 5 // 6


#Estados do jogador
STILL = 0
JUMPING = 1
FALLING = 2

class Player1(pygame.sprite.Sprite):
    
    
    def __init__(self, player1img):
        
         # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        #Inicia estado do jogador
        self.state = STILL
        
        # Carregando a imagem de fundo.
        self.image = player1img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player1img, (150, 150))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.left = 0 
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
        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy
        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND
            self.speedy = 0
            self.state = STILL
    
    def jump(self):
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING

            


class Player2(pygame.sprite.Sprite):
    
    
    def __init__(self, player2img):
        
         # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.state = STILL
        
        # Carregando a imagem de fundo.
        self.image = player2img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player2img, (150, 150))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.right = WIDTH 
        self.rect.bottom = HEIGHT - 10
        
        # Velocidade da nave
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
        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy
        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND
            self.speedy = 0
            self.state = STILL
    def jump(self):
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING
                



#carrega todos os assets                
def load_assets(img_dir, snd_dir):
    assets = {}
    assets["background"] = pygame.image.load(path.join(img_dir, 'Background.png')).convert()
    assets["player1img"] = pygame.image.load(path.join(img_dir, 'Player1.png')).convert()
    assets["player2img"] = pygame.image.load(path.join(img_dir, 'Player2.png')).convert()
    return assets





def game_screen(screen):
    #carrega assets
    assets = load_assets(img_dir, snd_dir)
    
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    
    #loada o fundo
    background = pygame.transform.scale(assets["background"],(WIDTH, HEIGHT))
    background_rect = background.get_rect()
    
    #Cria os jogadores
    player1 = Player1(assets["player1img"])
    player2 = Player2(assets["player2img"])
    
    
    #carrega os jogadores
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player1)
    all_sprites.add(player2)
     
    
        
    PLAYING = 0
    DONE = 1

    state = PLAYING
    while state != DONE:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        if state == PLAYING:
            # Processa os eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():
                
                # Verifica se foi fechado.
                if event.type == pygame.QUIT:
                    state = DONE
                    
                # Verifica se uma tecla foi apertada    
                if event.type == pygame.KEYDOWN :
                    # Teclas para o player 1
                    if event.key == pygame.K_w:
                        player1.jump()
                    if event.key == pygame.K_a:
                        player1.speedx = -3
                    if event.key == pygame.K_d:
                        player1.speedx = 3
                    if event.key == pygame.K_LEFT:
                        player2.speedx = -3
                    if event.key == pygame.K_RIGHT:
                        player2.speedx = 3
                    if event.key == pygame.K_UP:
                        player2.jump()
                
                
                if event.type == pygame.KEYUP:                  
                    if event.key == pygame.K_a:
                        player1.speedx = 0
                    if event.key == pygame.K_d:
                        player1.speedx = 0
                    if event.key == pygame.K_LEFT:
                        player2.speedx = 0
                    if event.key == pygame.K_RIGHT:
                        player2.speedx = 0
        
            
        
        
        # Atualiza a ação de cada sprite
        all_sprites.update()
        
        
        #Desenha o fundo skr
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        
        #Inverte o display
        pygame.display.flip()



        
        
# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("InsFighter")

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()
        
        

        
        
        
        
        
 
