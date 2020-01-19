import pygame, pygame_textinput, sys
from settings import Settings
from tools_parameters import *

clock = pygame.time.Clock()
pygame.init()
se = Settings()


def parameters_description():
    text_spindle_speed = se.font_tools.render('OBROTY na minutę',
                                              True,
                                              se.white)
    text_feed = se.font_tools.render('POSUW', True, se.white)
    se.screen.blit(text_feed, (160, 280))
    se.screen.blit(text_spindle_speed, (160, 220))

def table_description():
    #left titles
    text_vc_table = se.font_table.render('VC = 15', True, se.white)
    text_spindle_table = se.font_table.render('OBROTY', True, se.blue)
    text_hole = se.font_table.render('OTWÓR', True, se.blue)
    text_thread = se.font_table.render('SKOK', True, se.blue)
    text_tap_feed = se.font_table.render('POSUW', True, se.blue)

    se.screen.blit(text_vc_table, (45, 215))
    se.screen.blit(text_hole, (35, 265))
    se.screen.blit(text_thread, (35, 315))
    se.screen.blit(text_spindle_table, (35, 365))
    se.screen.blit(text_tap_feed, (35, 415))

    # bliting "m" dimensions
    dim = 2
    x_pos = 175
    text_tap_dim = se.font_table.render('M' + str(dim), True, se.orange)
    se.screen.blit(text_tap_dim, (x_pos, 215))

    for value in range(0, 4):
        dim += 1
        x_pos += 77
        text_tap_dim = se.font_table.render('M' + str(dim), True, se.orange)
        se.screen.blit(text_tap_dim, (x_pos, 215))
    for value in range(0, 3):
        dim += 2
        x_pos += 77
        text_tap_dim = se.font_table.render('M' + str(dim), True, se.orange)
        se.screen.blit(text_tap_dim, (x_pos, 215))

    # bliting spin parameters
    dim = 2
    x_pos = 172
    spin = drill_spin(dim, 15)
    text_dim = se.font_table.render(str(spin), True, se.white)
    se.screen.blit(text_dim, (x_pos, 365))

    for value in range(0, 4):
        dim += 1
        x_pos += 77
        spin = drill_spin(dim, 15)
        text_dim = se.font_table.render(str(spin), True, se.white)
        se.screen.blit(text_dim, (x_pos, 365))
    for value in range(0, 3):
        dim += 2
        x_pos += 77
        spin = drill_spin(dim, 15)
        text_dim = se.font_table.render(str(spin), True, se.white)
        se.screen.blit(text_dim, (x_pos, 365))

    # hole dimensions
    text_h_table = se.font_table.render('1,6', True, se.white)
    se.screen.blit(text_h_table, (175, 265))
    text_h_table = se.font_table.render('2,5', True, se.white)
    se.screen.blit(text_h_table, (252, 265))
    text_h_table = se.font_table.render('3,3', True, se.white)
    se.screen.blit(text_h_table, (329, 265))
    text_h_table = se.font_table.render('4,2', True, se.white)
    se.screen.blit(text_h_table, (406, 265))
    text_h_table = se.font_table.render('5,0', True, se.white)
    se.screen.blit(text_h_table, (483, 265))
    text_h_table = se.font_table.render('6,8', True, se.white)
    se.screen.blit(text_h_table, (560, 265))
    text_h_table = se.font_table.render('8,5', True, se.white)
    se.screen.blit(text_h_table, (637, 265))
    text_h_table = se.font_table.render('10,2', True, se.white)
    se.screen.blit(text_h_table, (714, 265))

    # thread dimensions
    text_th = se.font_table.render('0,25', True, se.white)
    se.screen.blit(text_th, (175, 315))
    text_th = se.font_table.render('0,5', True, se.white)
    se.screen.blit(text_th, (252, 315))
    text_th = se.font_table.render('0,7', True, se.white)
    se.screen.blit(text_th, (329, 315))
    text_th = se.font_table.render('0,8', True, se.white)
    se.screen.blit(text_th, (406, 315))
    text_th = se.font_table.render('1.0', True, se.white)
    se.screen.blit(text_th, (483, 315))
    text_th = se.font_table.render('1.25', True, se.white)
    se.screen.blit(text_th, (560, 315))
    text_th = se.font_table.render('1,5', True, se.white)
    se.screen.blit(text_th, (637, 315))
    text_th = se.font_table.render('1,75', True, se.white)
    se.screen.blit(text_th, (714, 315))

def cross_lines():
    '''Display lines on the cutter/drill screens'''
    pygame.draw.line(se.screen, se.white, (540, 200), (540, 450), 2)
    pygame.draw.line(se.screen, se.white, (150, 262), (650, 262), 1)
    pygame.draw.line(se.screen, se.white, (150, 324), (650, 324), 1)
    pygame.draw.line(se.screen, se.white, (150, 386), (650, 386), 1)

def table():
    '''Display lines on the parameter screen'''
    x = 165
    y = 250
    pygame.draw.line(se.screen, se.white, (x, 200), (x, 450), 3)
    for value in range(0, 7):
        x += 77
        pygame.draw.line(se.screen, se.white, (x, 200), (x, 450), 1)

    pygame.draw.line(se.screen, se.white, (25, y), (775, y), 3)
    for value in range(0, 4):
        y += 50
        pygame.draw.line(se.screen, se.white, (25, y), (775, y), 1)

def cutter_push_button(x, y, w, h, action=None):
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

def tap_push_button(x, y, w, h, action=None):
    '''Making a flashing cutter button '''

    # x: The x location of the top left coordinate of the button box.
    # y: The y location of the top left coordinate of the button box.
    # w: Button width.
    # h: Button height.

    pygame.font.init()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        se.screen.blit(se.tap_white, (x, y))
        if click[0] == 1 and action != None:
            action()
    else:
        se.screen.blit(se.tap_button, (x, y))

def drill_push_button(x, y, w, h, action=None):
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

def back_button(x, y, w, h):
    '''Making a flashing return button'''
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
        cross_lines()
        parameters_description()
        txtinput.update(events)
        if diameter:
            # calculating and display drill spining parameter
            font_drill_spin = pygame.font.Font('freesansbold.ttf', 30)
            text_drill_spin = font_drill_spin.render(str(drill_spin(
                diameter)), True, (250, 250, 250))
            se.screen.blit(text_drill_spin, (550, 220))
            # calculating and display drill feed parameter
            font_drill_feed = pygame.font.Font('freesansbold.ttf', 30)
            text_drill_feed = font_drill_feed.render(str(drill_feed(
                diameter)), True, (250, 250, 250))
            se.screen.blit(text_drill_feed, (550, 282))
        se.screen.blit(txtinput.get_surface(), (50, 126))
        if back_button(700, 0, 100, 100):
            break
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
        parameters_description()
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
            se.screen.blit(text_cutter_feed, (550, 344))

            font_cutter_feed = pygame.font.Font('freesansbold.ttf', 30)
            text_cutter_feed = font_cutter_feed.render(str(cutter_feed(
                diameter)), True, (250, 250, 250))
            se.screen.blit(text_cutter_feed, (550, 282))
        se.screen.blit(txtinput.get_surface(), (50, 126))
        if back_button(700, 0, 100, 100):
            break
        pygame.display.flip()

def tap_parameter_loop():
    se = Settings()
    parameter = True

    while parameter:
        clock.tick(30)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                parameter = False

        se.screen.blit(se.bg, (0, 0))
        pygame.draw.rect(se.screen, se.black, (200, 20, 400, 55))
        pygame.draw.rect(se.screen, se.white, (200, 20, 400, 55), 2)
        pygame.draw.rect(se.screen, se.black, (25, 200, 750, 250))
        pygame.draw.rect(se.screen, se.white, (25, 200, 750, 250), 3)
        table()
        table_description()
        se.screen.blit(se.text_tap_menu, (225, 25))
        if back_button(700, 0, 100, 100):
            break
        pygame.display.update()

tap_parameter_loop()