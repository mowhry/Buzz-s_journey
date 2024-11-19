import  pygame
from pygame.locals import *
from menu import MainMenu

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.WINDOW_W, self.WINDOW_H = 1200, 800
        self.display = pygame.Surface((self.WINDOW_W, self.WINDOW_H))
        self.window = pygame.display.set_mode(((self.WINDOW_W, self.WINDOW_H)))
        self.font_name = "./assets/Gamepaused.otf"
        self.current_menu = MainMenu(self)

    def game_loop(self):
        while self.playing:
            self.check_event()
            if self.START_KEY:
                self.playing = False
            self.display.fill((0, 0, 0))
            self.draw_text("Thanks for Playing", 20, self.WINDOW_W/2, self.WINDOW_H/2)
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

    def reset_key(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
