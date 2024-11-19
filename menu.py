import  pygame
from pygame.locals import *

class Menu():
    def __init__(self,  game):
        self.game = game
        self.mid_w, self.mid_h = self.game.WINDOW_W/2, self.game.WINDOW_H/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text("x", 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_key()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionx, self.optiony = self.mid_w, self.mid_h + 50
        self.creditx, self.credity = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_event()
            self.check_input()
            self.game.display.fill((0, 0 ,0))
            self.game.draw_text("Main Menu", 20, self.game.WINDOW_W/2, self.game.WINDOW_H/2 - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Options", 20, self.optionx, self.optiony)
            self.game.draw_text("Credits", 20, self.creditx, self.credity)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.optionx + self.offset, self.optiony)
                self.state = "Options"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.creditx + self.offset, self.credity)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
        elif self.game.UP_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.creditx + self.offset, self.credity)
                self.state = "Credits"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.optionx + self.offset, self.optiony)
                self.state = "Options"

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Start":
                self.game.playing = True
            elif self.state == "Options":
                self.game.current_menu = self.game.options_menu
            elif self.state == "Credits":
                self.game.current_menu = self.game.credits_menu
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Volume"
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlx, self.controly = self.mid_w, self.mid_h + 40

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_event()
            self.check_input()
            self.game.display.fill((0, 0 ,0))
            self.game.draw_text("Options", 40, self.game.WINDOW_W / 2, self.game.WINDOW_H / 2 - 30)
            self.game.draw_text("Volume", 20, self.volx, self.voly)
            self.game.draw_text("Controls", 20, self.controlx, self.controly)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.current_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == "Volume":
                self.state = "Controls"
                self.cursor_rect.midtop = (self.controlx + self.offset, self.controly)
            elif self.state == "Controls":
                self.state = "Volume"
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            #to do volume/controle
            pass

class CreditMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Credit"
        self.credx, self.credy = self.mid_w, self.mid_h + 20
        self.px, self.py = self.mid_w, self.mid_h + 50
        self.p2x, self.p2y = self.mid_w, self.mid_h + 70

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_event()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.current_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill((0, 0, 0))
            self.game.draw_text("Credits", 30, self.credx, self.credy)
            self.game.draw_text("Made by Mowhry with love", 20, self.px, self.py)
            self.game.draw_text("You can drop a star on this repo !", 20, self.p2x, self.p2y)
            self.blit_screen()
