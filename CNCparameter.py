import pygame
import sys
import time
from settings import Settings
from buttons_actions import *

se = Settings()
pygame.mouse.set_visible(True)
pygame.init()

def run_menu():
    pygame.display.set_caption('CNC Parameter')
    menu = True

    while menu:
        # obsługa eventów
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

        # rysowanie
        se.screen.blit(se.bg, (0, 0))
        se.screen.blit(se.text_tools, se.text_toolsRect)
        se.screen.blit(se.text_cnc, se.text_cncRect)
        drill_push_button(450, 300, 300, 143, drill_parameter_loop)
        cutter_push_button(50, 300, 300, 143, cutter_parameter_loop)
        se.clock.tick(15)
        pygame.display.update()

if __name__ == "__main__":
    run_menu()