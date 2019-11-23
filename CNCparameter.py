import pygame
import sys
import time
time.time()
from pygame.locals import *

pygame.init()   # warto wczytać defaultowo
pygame.font.init()

# test
# background image load
bg = pygame.image.load('images/bg_cnc.png')
frez_button = pygame.image.load('images/frez.png')
frez_white_button = pygame.image.load('images/frez_white.png')
drill_white_button = pygame.image.load('images/drill_white.png')
drill_button = pygame.image.load('images/drill.png')
pygame.display.set_caption("CNC Parameter")

# colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (100, 240, 240)
red = (250,0,0)

# screen resolution
X = 800
Y = 500


screen = pygame.display.set_mode((X,Y))
clock = pygame.time.Clock()


font_cnc = pygame.font.Font('freesansbold.ttf', 60)
font_tools = pygame.font.Font('freesansbold.ttf', 30)
text_cnc = font_cnc.render('CNC Parameter', True, white)
text_tools = font_tools.render('WYBIERZ RODZAJ NARZĘDZIA', True, white)

font_cutter_menu = pygame.font.Font('freesansbold.ttf', 50)
font_drill_menu = pygame.font.Font('freesansbold.ttf', 50)
text_cutter_menu = font_cutter_menu.render('FREZ VHM', True, white)
text_drill_menu = font_cutter_menu.render('WIERTŁO HSS', True,
                                          white)

text_cncRect = text_cnc.get_rect()
text_cncRect.center = (X / 2, Y -450)

text_toolsRect = text_tools.get_rect()
text_toolsRect.center = (X // 2, Y -250)

text_cutter_menuRect = text_cutter_menu.get_rect()
text_cutter_menuRect.center = (X / 2, Y -450)

text_drill_menuRect = text_drill_menu.get_rect()
text_drill_menuRect.center = (X / 2, Y -450)

pygame.mouse.set_visible(True)



def drill_parameter(diameter, vc = 35):
    '''Parametry dla wierteł, zwraca obroty i posuw mm/min'''
    d = diameter
    fz = 0.1
    # obroty na minutę
    n = (1000.0 * vc) / (float(d) * 3.14)
    # posuw mm/min
    if diameter in range(0,5):
        fz = 0.1
    elif diameter in range(4,9):
        fz = 0.18
    else:
        fz = 0.22
    f = fz * n
    return int(n), int(f)


def cutter_parameter(diameter, vc = 400):
    '''Parametry dla frezów, zwraca obroty i posuw mm/min '''
    d = diameter
    fz = 0.02

    # obroty na minutę
    n = (1000.0 * vc)/(float(d) * 3.14)
    if n > 22000:
        n = 22000
    # posuw mm/min
    f = fz * n
    return int(n), int(f)

def cutter_push_button(x,y,w,h,action = None):

    # x: The x location of the top left coordinate of the button box.
    # y: The y location of the top left coordinate of the button box.
    # w: Button width.
    # h: Button height.

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        screen.blit(frez_white_button, (x, y))

        if click[0] == 1 and action != None:
            action()
    else:
        screen.blit(frez_button, (x, y))

def drill_push_button(x,y,w,h,action = None):
    # x: The x location of the top left coordinate of the button box.
    # y: The y location of the top left coordinate of the button box.
    # w: Button width.
    # h: Button height.
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        screen.blit(drill_white_button, (x, y))
        if click[0] == 1 and action != None:
            action()

    else:
        screen.blit(drill_button, (x, y))

def drill_parameter_loop():

    font = pygame.font.Font(None, 32)
    active = False
    input_box = pygame.Rect(550, 150, 140, 32)
    parameter = True
    color_inactive = pygame.Color('white')
    color_active = pygame.Color('white')
    color = color_inactive
    text = ''

    while parameter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                menu_loop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(bg, (0, 0))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(text_drill_menu, text_drill_menuRect)
        pygame.draw.rect(screen, white, (50, 390, 240, 32))
        pygame.draw.rect(screen, white, (500, 390, 240, 32))
        pygame.display.update()
        clock.tick(15)

def cutter_parameter_loop():
    parameter = True
    while parameter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                menu_loop()
        screen.blit(bg,(0,0))
        screen.blit(text_cutter_menu, text_cutter_menuRect)
        pygame.draw.rect(screen, white, (500,400,250,50))
        pygame.display.update()
        clock.tick(15)

def menu_loop():

    menu = True

    while menu:
        # obsługa eventów
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

        # rysowanie
        screen.blit(bg, (0, 0))
        screen.blit(text_tools, text_toolsRect)
        screen.blit(text_cnc, text_cncRect)
        drill_push_button(450,300,300,143,drill_parameter_loop)
        cutter_push_button(50,300,300,143,cutter_parameter_loop)
        pygame.display.update()
        clock.tick(15)

if __name__ == '__main__':
    menu_loop()
