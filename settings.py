import pygame
pygame.font.init()
from tools_parameters import *

class Settings():
    '''Parameters for main program'''

    def __init__(self):
        # colors
        self.white = (255, 255, 255)
        self.black = (22,22,20)
        self.blue = (100, 240, 240)
        self.red = (250, 0, 0)
        self.blue = (88, 131, 176)
        self.orange = (202, 178, 72)

        # screen resolution
        self.screen_width = 800
        self.screen_hight = 500

        # fonts
        self.font_cnc = pygame.font.Font('freesansbold.ttf', 60)
        self.font_tools = pygame.font.Font('freesansbold.ttf', 30)
        self.font_cutter_menu = pygame.font.Font('freesansbold.ttf', 50)
        self.font_drill_menu = pygame.font.Font('freesansbold.ttf', 50)
        self.font_table = pygame.font.Font('freesansbold.ttf', 25)

        #frames
        self.frame_menu = pygame.Rect(165, 13, 470, 66)
        self.frame_vhm = pygame.Rect(250, 20, 290, 55)
        self.frame_drill = pygame.Rect(210, 20, 380, 55)
        self.frame_txtinput = pygame.Rect(40, 120, 390, 36)
        self.frame_results = pygame.Rect(150, 200, 500, 250)

        # text
        self.text_cnc = self.font_cnc.render('CNC Parameter', True, self.white)
        self.text_tools = self.font_tools.render('WYBIERZ RODZAJ NARZĘDZIA',
                                               True, self.white)
        self.text_cutter_menu = self.font_cutter_menu.render('FREZ VHM', True,
                                                        self.white)
        self.text_drill_menu = self.font_cutter_menu.render('WIERTŁO HSS',
                                                            True,
                                                  self.white)
        self.text_tap_menu = self.font_cutter_menu.render('GWINTOWNIK',
                                                            True,
                                                  self.white)

        # load images
        self.bg = pygame.image.load('images/bg_cnc.png')
        self.frez_button = pygame.image.load('images/frez.png')
        self.frez_white_button = pygame.image.load('images/frez_white.png')
        self.drill_white_button = pygame.image.load('images/drill_white.png')
        self.drill_button = pygame.image.load('images/drill.png')
        self.back = pygame.image.load('images/back.png')
        self.back_white = pygame.image.load('images/back_white.png')
        self.tap_button = pygame.image.load('images/thread.png')
        self.tap_white = pygame.image.load('images/thread_white.png')

        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_hight))
        self.fake_screen = self.screen.copy()
        self.clock = pygame.time.Clock()
        self.text_cncRect = self.text_cnc.get_rect()
        self.text_cncRect.center = (self.screen_width / 2, self.screen_hight
                                    - 450)

        self.text_toolsRect = self.text_tools.get_rect()
        self.text_toolsRect.center = (self.screen_width // 2,
                                      self.screen_hight - 360)

        self.text_cutter_menuRect = self.text_cutter_menu.get_rect()
        self.text_cutter_menuRect.center = (self.screen_width / 2,
                                            self.screen_hight -
                                            450)

        self.text_drill_menuRect = self.text_drill_menu.get_rect()
        self.text_drill_menuRect.center = (self.screen_width / 2,
                                           self.screen_hight - 450)
