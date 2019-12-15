import pygame
from settings import Settings
pygame.init()

se = Settings()

def cutter_push_button(x,y,w,h,action = None):
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


def drill_push_button(x,y,w,h,action = None):
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
                parameter = False
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
        se.screen.blit(se.bg, (0, 0))
        se.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(se.screen, color, input_box, 2)
        se.screen.blit(se.text_drill_menu, se.text_drill_menuRect)
        pygame.draw.rect(se.screen, se.white, (50, 390, 240, 32))
        pygame.draw.rect(se.screen, se.white, (500, 390, 240, 32))
        pygame.display.update()

def cutter_parameter_loop():
    se = Settings()
    parameter = True
    while parameter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                parameter = False

        se.screen.blit(se.bg,(0,0))
        se.screen.blit(se.text_cutter_menu, se.text_cutter_menuRect)
        pygame.draw.rect(se.screen, se.white, (500,400,250,50))
        pygame.display.update()
        se.clock.tick(15)
