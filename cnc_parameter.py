import pygame
import sys
from settings import Settings
from buttons_actions import *

clock = pygame.time.Clock()
pygame.display.set_caption('CNC Parameter')
pygame.mouse.set_visible(True)
se = Settings()


def run_menu():
    pygame.init()
    clock.tick(30)
    menu = True

    while menu:
        # obsługa eventów
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

        # drawing
        se.screen.blit(se.bg, (0, 0))
        pygame.draw.rect(se.screen, se.black, (165, 13, 470, 66),2)
        pygame.draw.rect(se.screen, se.black, (170, 248, 460, 40))
        pygame.draw.rect(se.screen, se.white, (170, 248, 460, 40), 1)
        pygame.draw.rect(se.screen, se.white, se.frame_menu, 3)
        se.screen.blit(se.text_tools, se.text_toolsRect)
        se.screen.blit(se.text_cnc, se.text_cncRect)
        drill_push_button(450, 300, 300, 143, drill_parameter_loop)
        cutter_push_button(50, 300, 300, 143, cutter_parameter_loop)
        pygame.display.update()

if __name__ == "__main__":
    run_menu()