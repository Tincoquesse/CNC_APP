import pygame
pygame.font.init()

class Settings():

    '''Parameters for main program'''

    def __init__(self):
        # colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.blue = (100, 240, 240)
        self.red = (250, 0, 0)

        # screen resolution
        self.screen_width = 800
        self.screen_hight = 500

        # fonts
        self.font_cnc = pygame.font.Font('freesansbold.ttf', 60)
        self.font_tools = pygame.font.Font('freesansbold.ttf', 30)
        self.font_cutter_menu = pygame.font.Font('freesansbold.ttf', 50)
        self.font_drill_menu = pygame.font.Font('freesansbold.ttf', 50)

        # text
        self.text_cnc = self.font_cnc.render('CNC Parameter', True, self.white)
        self.text_tools = self.font_tools.render('WYBIERZ RODZAJ NARZĘDZIA',
                                               True, self.white)
        self.text_cutter_menu = self.font_cutter_menu.render('FREZ VHM', True,
                                                        self.white)
        self.text_drill_menu = self.font_cutter_menu.render('WIERTŁO HSS',
                                                            True,
                                                  self.white)

        # images load
        self.bg = pygame.image.load('images/bg_cnc.png')
        self.frez_button = pygame.image.load('images/frez.png')
        self.frez_white_button = pygame.image.load('images/frez_white.png')
        self.drill_white_button = pygame.image.load('images/drill_white.png')
        self.drill_button = pygame.image.load('images/drill.png')


        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_hight))
        self.clock = pygame.time.Clock()
        self.text_cncRect = self.text_cnc.get_rect()
        self.text_cncRect.center = (self.screen_width / 2, self.screen_hight
                                    - 450)

        self.text_toolsRect = self.text_tools.get_rect()
        self.text_toolsRect.center = (self.screen_width // 2,
                                      self.screen_hight - 250)

        self.text_cutter_menuRect = self.text_cutter_menu.get_rect()
        self.text_cutter_menuRect.center = (self.screen_width / 2,
                                            self.screen_hight -
                                            450)

        self.text_drill_menuRect = self.text_drill_menu.get_rect()
        self.text_drill_menuRect.center = (self.screen_width / 2,
                                           self.screen_hight - 450)
