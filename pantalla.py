import sys
import pygame

class paintxel:
    #def __init__(self):  # Atributos
        pygame.init()
        tpantalla = (1000,700)
        cfondo = (247, 249, 249)
        clinea = (179, 182, 183)
        screen = pygame.display.set_mode(tpantalla)
        pygame.display.set_caption("PAINTXEL")
        screen.fill(cfondo)

        while True: #para que la pantalla se mantenga
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update() # actualizar pantalla