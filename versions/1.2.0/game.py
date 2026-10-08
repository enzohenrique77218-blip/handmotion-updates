import pygame
import sys

pygame.init()

LARGURA = 900
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("HandMotion - VERSÃO 1.2.0")

FUNDO = (25, 35, 65)
BRANCO = (255, 255, 255)
AZUL = (80, 180, 255)
VERDE = (100, 255, 150)

fonte_titulo = pygame.font.SysFont("arial", 46, bold=True)
fonte_versao = pygame.font.SysFont("arial", 28, bold=True)
fonte_mensagem = pygame.font.SysFont("arial", 23, bold=True)
fonte_detalhe = pygame.font.SysFont("arial", 18)

relogio = pygame.time.Clock()

executando = True

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    tela.fill(FUNDO)

    titulo = fonte_titulo.render("HANDMOTION", True, BRANCO)
    versao = fonte_versao.render("VERSÃO 1.2.0", True, VERDE)
    mensagem = fonte_mensagem.render(
        "ATUALIZAÇÃO ONLINE CONCLUÍDA!",
        True,
        BRANCO,
    )
    detalhe = fonte_detalhe.render(
        "Este jogo foi baixado automaticamente do GitHub Pages.",
        True,
        AZUL,
    )

    tela.blit(titulo, titulo.get_rect(center=(LARGURA // 2, 210)))
    tela.blit(versao, versao.get_rect(center=(LARGURA // 2, 290)))
    tela.blit(mensagem, mensagem.get_rect(center=(LARGURA // 2, 360)))
    tela.blit(detalhe, detalhe.get_rect(center=(LARGURA // 2, 410)))

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
sys.exit()
