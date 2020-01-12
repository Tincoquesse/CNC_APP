'''Functions needed to create the button'''

import pygame, pygame_textinput, sys
from settings import Settings
from tools_parameters import *

clock = pygame.time.Clock()
pygame.init()
se = Settings()

def cross_lines():
    # display lines on the parameter screen
    pygame.draw.line(se.screen, se.white,(540,200),(540,450),2 )
    pygame.draw.line(se.screen, se.white, (150, 262), (650, 262), 1)
    pygame.draw.line(se.screen, se.white, (150, 324), (650, 324), 1)
    pygame.draw.line(se.screen, se.white, (150, 386), (650, 386), 1)

def cutter_push_button(x,y,w,h,action=None):
    '''Making a flashing cutter button '''

    # x: The x location of the top left coordinate of the button box.
    # y: The y location of the top left coordinate of the button box.
    # w: Button width.
    # h: Button height.

    pygame.font.init()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        se.screen.blit(se.frez_white_button, (x, y))
        if click[0] == 1 and action != None:
            action()
    else:
        se.screen.blit(se.frez_button, (x, y))

def drill_push_button(x,y,w,h,action=None):
    '''Making a flashing drill button'''
    # x: The x location of the top left coordinate of the button box.
    # y: The y location of the top left coordinate of the button box.
    # w: Button width.
    # h: Button height.
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        se.screen.blit(se.drill_white_button, (x, y))
        if click[0] == 1 and action != None:
            action()

    else:
        se.screen.blit(se.drill_button, (x, y))

def back_button(x ,y ,w ,h):

    '''Making a flashing drill button'''
    # x: The x location of the top left coordinate of the button box.
    # y: The y location of the top left coordinate of the button box.
    # w: Button width.
    # h: Button height.
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        se.screen.blit(se.back_white, (x, y))
        if click[0] == 1:
            return True
    else:
        se.screen.blit(se.back, (x, y))

def drill_parameter_loop():
    se = Settings()
    diameter = int()
    txtinput = pygame_textinput.TextInput()
    parameter = True

    while parameter:
        clock.tick(30)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                parameter = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                txt = txtinput.get_text()
                if len(txt) > 20:
                    try:
                        diameter = float(txt[20:])
                    except ValueError:
                        pass
        se.screen.blit(se.bg, (0, 0))
        pygame.draw.rect(se.screen, se.black, (210, 20, 380, 55))
        pygame.draw.rect(se.screen, se.white, se.frame_drill, 2)
        pygame.draw.rect(se.screen, se.black, (40, 120, 390, 36))
        pygame.draw.rect(se.screen, se.white, se.frame_txtinput, 1)
        pygame.draw.rect(se.screen, se.black, (150, 200, 500, 250))
        pygame.draw.rect(se.screen, se.white, se.frame_results, 3)
        se.screen.blit(se.text_drill_menu, se.text_drill_menuRect)
        txtinput.update(events)
        if diameter:
            # calculating and display drill spin parameters
            font_drill_spin = pygame.font.Font('freesansbold.ttf', 30)
            text_drill_spin = font_drill_spin.render(str(drill_spin(
                diameter)), True, (250, 250, 250))
            se.screen.blit(text_drill_spin, (550, 220))
            # calculating and display dtill feed parameter
            font_drill_feed = pygame.font.Font('freesansbold.ttf', 30)
            text_drill_feed = font_drill_feed.render(str(drill_feed(
                diameter)), True, (250, 250, 250))
            se.screen.blit(text_drill_feed, (550, 350))
        se.screen.blit(txtinput.get_surface(), (50, 126))
        if back_button(700, 0, 100, 100):
            break
        cross_lines()
        pygame.display.update()

def cutter_parameter_loop():
    se = Settings()
    diameter = int()
    txtinput = pygame_textinput.TextInput()
    parameter = True

    while parameter:
        clock.tick(30)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                parameter = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                txt = txtinput.get_text()
                if len(txt) > 20:
                    try:
                        diameter = float(txt[20:])
                    except ValueError:
                        pass
        se.screen.blit(se.bg, (0, 0))
        pygame.draw.rect(se.screen, se.black, (250, 20, 290, 55))
        pygame.draw.rect(se.screen, se.white, se.frame_vhm, 2)
        pygame.draw.rect(se.screen, se.black, (40, 120, 390, 36))
        pygame.draw.rect(se.screen, se.white, se.frame_txtinput, 1)
        pygame.draw.rect(se.screen, se.black, (150, 200, 500, 250))
        pygame.draw.rect(se.screen, se.white, se.frame_results, 3)
        se.screen.blit(se.text_cutter_menu, se.text_cutter_menuRect)
        cross_lines()
        txtinput.update(events)
        if diameter:

            font_cutter_spin = pygame.font.Font('freesansbold.ttf', 30)
            text_cutter_spin = font_cutter_spin.render(str(cutter_spin(
                diameter)), True, (250, 250, 250))
            se.screen.blit(text_cutter_spin, (550, 220))

            font_cutter_feed = pygame.font.Font('freesansbold.ttf', 30)
            cut_feed = cutter_feed_hundred(diameter)
            text_cutter_feed = font_cutter_feed.render(str(cut_feed)[0:3],
                                                       True,
                                                       (250, 250, 250))
            se.screen.blit(text_cutter_feed, (550, 280))

            font_cutter_feed = pygame.font.Font('freesansbold.ttf', 30)
            text_cutter_feed = font_cutter_feed.render(str(cutter_feed(
                diameter)),True,(250,250,250))
            se.screen.blit(text_cutter_feed, (550,350))
        se.screen.blit(txtinput.get_surface(), (50,126))
        if back_button(700, 0, 100, 100):
            break
        pygame.display.flip()


cutter_parameter_loop()