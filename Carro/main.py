import pygame  # indica que utilizaremos pygame
from scripts.cenas import Partida
from scripts.cenas import Menu

pygame.init()  # inicia o pygame

tamanhoTela = [350, 500]  # define o tamanho da janela do jogo
tela = pygame.display.set_mode(tamanhoTela)  # cria a janela que utilizaremos
pygame.display.set_caption("Car Game")  # define o título da janela
relogio = pygame.time.Clock()  # cria um relógio para controlar a velocidade do jogo
corFundo = (0, 0, 0)  # cria uma cor de fundo em formato RGB

# Variável para criar o efeito de movimento na pista
offset_pista = 0
velocidade_pista = 5  # Velocidade da pista

def desenhar_pista(tela, offset):
    # Desenhar a pista preta
    pygame.draw.rect(tela, (0, 0, 0), (50, 0, 250, 500))  # Pista preta centralizada
    

# Loop principal do jogo
listaCenas = {
    'partida': Partida(tela),  # Passa as calçadas para a Partida
    'menu': Menu(tela)
}

cenaAtual = 'menu'
while True:  # cria um laço infinito para manter o jogo aberto
    for e in pygame.event.get():  # laço que passa em cada evento do pygame
        if e.type == pygame.QUIT:  # verifica se é do tipo sair; que ocorre quando fecha a tela
            pygame.quit()  # finaliza o pygame

    tela.fill(corFundo)  # Limpa a tela com a cor de fundo

    # Atualiza o offset para criar o efeito de movimento
    offset_pista += velocidade_pista
    if offset_pista >= 40:  # Reseta o offset para loop da faixa
        offset_pista = 0

    desenhar_pista(tela, offset_pista)  # Desenha a pista com o offset

    # Atualiza e desenha o jogador
    cenaAtual = listaCenas[cenaAtual].atualizar()
    relogio.tick(60)  # controla a tela para atualizar 60 vezes por segundo
    pygame.display.flip()  # atualiza a tela, mostrando as alterações feitas
