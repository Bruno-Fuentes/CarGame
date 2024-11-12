import pygame
import random # importamos a função que gera números aleatórios

# Classe
class Cano:
    def __init__(self,tela):
        self.imagem = pygame.image.load('assets/cano.png') #Carregamos a imagem
        self.tela = tela # definimos a tela
        self.altura_base = random.randint(100,300) # geramos um número aleatório para a altura da base do
        self.x = tela.get_width() # define a posição x com a largura tela, ou seja no lado direito
        self.distancia = 50 # define a distância entre o cano de cima e o cano de baixo
        self.cano_cima = self.altura_base - self.imagem.get_height()-self.distancia 
        #definimos a altura do cano de cima, como a altura base, menos a altura da imagem, menos a distancia
        self.cano_baixo = self.altura_base + self.distancia # definimos a altura do cano de baixo como a altura
        # para o cano ficar pra baixo
        self.velocidade = 2 # velocidade em que o cano se move para esquerda

    def atualizar(self):
        self.x -= self.velocidade # aplica velocidade na posicao
        if self.x <= -self.imagem.get_width(): # verifica se a imagem toda saiu da tela,
            self.x = self.tela.get_width() # volta para a direita
            self.altura_base = random.randint(100,300) # usa a função randint para criar uma nova altura base
            self.cano_cima = self.altura_base - self.imagem.get_height()-self.distancia
            self.cano_baixo = self.altura_base + self.distancia
        # atualiza a posicao de ambos os canos

    def desenhar(self):
        imagem_invertida = pygame.transform.flip(self.imagem,False,True) # faz o cano ficar invertido vert
        self.tela.blit(imagem_invertida,(self.x,self.cano_cima))
        self.tela.blit(self.imagem,(self.x,self.cano_baixo))
        # desenha o cano invertido e o normal na tela

    def detectarColisao(self, rectJogador): 
        rectCanoCima = pygame.Rect((self.x, self.cano_cima), self.imagem.get_size())
        rectCanoBaixo = pygame.Rect((self.x, self.cano_baixo), self.imagem.get_size())
        
        if rectJogador.colliderect(rectCanoCima) or rectJogador.colliderect(rectCanoBaixo):
            return True
        else:
            return False

