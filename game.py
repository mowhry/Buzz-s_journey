import  pygame, sys, time
from pygame.locals import *
from menu import *

class Game():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("./assets/Jake_Lake_Final_Refuge.wav")
        pygame.mixer.music.play(loops=-1, start=1, fade_ms=0)
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESC_KEY = False, False, False, False, False
        self.WINDOW_W, self.WINDOW_H = 1200, 800
        self.display = pygame.Surface((self.WINDOW_W, self.WINDOW_H))
        self.window = pygame.display.set_mode(((self.WINDOW_W, self.WINDOW_H)))
        self.font_name = "./assets/Daydream.ttf"
        self.main_menu = MainMenu(self)
        self.options_menu = OptionsMenu(self)
        self.credits_menu = CreditMenu(self)
        self.current_menu = self.main_menu
        self.backgrounds = [
            pygame.image.load(f"./assets/Clouds/Clouds_4/{i}.png").convert_alpha()
            for i in range(1, 5, 1)
        ]
        self.backgrounds = [pygame.transform.scale(bg, (self.WINDOW_W, self.WINDOW_H)) for bg in self.backgrounds]

        self.nightybg = [
            pygame.image.load(f"./assets/Clouds/Clouds_3/{i}.png").convert_alpha()
            for i in range(1, 5, 1)
        ]
        self.nightybg = [pygame.transform.scale(bg, (self.WINDOW_W, self.WINDOW_H)) for bg in self.nightybg]

        self.dawnbg = [
            pygame.image.load(f"./assets/Clouds/Clouds_2/{i}.png").convert_alpha()
            for i in range(1, 5, 1)
        ]
        self.dawnbg = [pygame.transform.scale(bg, (self.WINDOW_W, self.WINDOW_H)) for bg in self.dawnbg]

    def game_loop(self):
        while self.playing:
            self.check_event()
            if self.ESC_KEY:
                self.playing = False
            self.display.fill((0, 0, 0))
            for bg in self.backgrounds:
                self.display.blit(bg, (0,0))
            self.draw_text("Thanks for Playing", 20, self.WINDOW_W/2, self.WINDOW_H/2, (255, 255, 255))
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_key()

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.current_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.ESC_KEY = True

    def reset_key(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESC_KEY = False, False, False, False, False

    def draw_text(self, text, size, x, y, color, line_spacing = 1):
        font = pygame.font.Font(self.font_name, size)
        lines = text.split("\n")
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, color)
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y + i * (size + line_spacing))
            self.display.blit(text_surface, text_rect)
