import  pygame
from pygame.locals import *

class Menu():
    def __init__(self,  game):
        self.game = game
        self.mid_w, self.mid_h = self.game.WINDOW_W/2, self.game.WINDOW_H/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -150

    # def draw_cursor(self):
    #     self.game.draw_text("x", 15, self.cursor_rect.x, self.cursor_rect.y, (232, 135, 183))

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_key()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h
        self.optionx, self.optiony = self.mid_w, self.mid_h + 50
        self.creditx, self.credity = self.mid_w, self.mid_h + 100
        self.exitx, self.exity = self.mid_w, self.mid_h + 150
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

        self.start_color = (255, 255, 255)
        self.option_color = (255, 255, 255)
        self.credit_color = (255, 255, 255)
        self.exit_color = (255, 255, 255)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_event()
            self.check_input()
            self.game.display.fill((0, 0 ,0))
            for bg in self.game.backgrounds:
                self.game.display.blit(bg, (0, 0))
            self.game.draw_text("Main Menu", 60, self.game.WINDOW_W/2, self.game.WINDOW_H/2 - 100, (255, 255, 255))

            self.start_color = (232, 135, 183) if self.state == "Start" else (255, 255, 255)
            self.option_color = (232, 135, 183) if self.state == "Options" else (255, 255, 255)
            self.credit_color = (232, 135, 183) if self.state == "Credits" else (255, 255, 255)
            self.exit_color = (232, 135, 183) if self.state == "Exit" else (255, 255, 255)

            self.game.draw_text("Start Game", 40, self.startx, self.starty, (self.start_color))
            self.game.draw_text("Options", 40, self.optionx, self.optiony, (self.option_color))
            self.game.draw_text("Credits", 40, self.creditx, self.credity, (self.credit_color))
            self.game.draw_text("Exit", 40, self.exitx, self.exity, (self.exit_color))
            # self.draw_cursor()
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
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = "Exit"
            elif self.state == "Exit":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
        elif self.game.UP_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = "Exit"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.optionx + self.offset, self.optiony)
                self.state = "Options"
            elif self.state == "Exit":
                self.cursor_rect.midtop = (self.creditx + self.offset, self.credity)
                self.state = "Credits"

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Start":
                self.game.playing = True
            elif self.state == "Options":
                self.game.current_menu = self.game.options_menu
            elif self.state == "Credits":
                self.game.current_menu = self.game.credits_menu
            elif self.state == "Exit":
                self.game.running, self.game.playing = False, False
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Volume"
        self.volx, self.voly = self.mid_w, self.mid_h + 50
        self.controlx, self.controly = self.mid_w, self.mid_h + 100

        self.volume_color = (255, 255, 255)
        self.control_color = (255, 255, 255)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_event()
            self.check_input()
            self.game.display.fill((0, 0 ,0))
            for bg in self.game.dawnbg:
                self.game.display.blit(bg, (0, 0))

            self.volume_color = (232, 135, 183) if self.state == "Volume" else (255, 255, 255)
            self.control_color = (232, 135, 183) if self.state == "Controls" else (255, 255, 255)

            self.game.draw_text("Options", 70, self.game.WINDOW_W / 2, self.game.WINDOW_H / 2 - 30, (255, 255, 255))
            self.game.draw_text("Volume", 40, self.volx, self.voly, (self.volume_color))
            self.game.draw_text("Controls", 40, self.controlx, self.controly, (self.control_color))
            # self.draw_cursor()
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
        self.px, self.py = self.mid_w, self.mid_h + 40

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_event()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.current_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill((0, 0, 0))
            for bg in self.game.nightybg:
                self.game.display.blit(bg, (0, 0))
            self.game.draw_text("Credits", 60, self.game.WINDOW_W/2, self.game.WINDOW_H/2 - 30, (255, 255, 255))
            self.game.draw_text("Music: Jake Lake - Final Refuge\nCoded by Jessim Skiba with buzz sleeping on my desk\nYou can drop a star on this repo !", 15, self.px, self.py, (255, 255, 255))
            self.blit_screen()
