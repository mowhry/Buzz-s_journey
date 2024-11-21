import  pygame
import  sys
from    pygame.locals import *
from    menu import *
from    map import *
from    level import *
from    player import *

class Game():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.mixer.init()
        pygame.mixer.music.load("./assets/Jake_Lake_Final_Refuge.wav")
        pygame.mixer.music.play(loops=-1, start=1, fade_ms=0)
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESC_KEY = False, False, False, False, False
        self.WINDOW_W, self.WINDOW_H = 1216, 800
        self.display = pygame.Surface((self.WINDOW_W, self.WINDOW_H))
        self.window = pygame.display.set_mode(((self.WINDOW_W, self.WINDOW_H)))
        self.font_name = "./assets/Daydream.ttf"
        self.main_menu = MainMenu(self)
        self.options_menu = OptionsMenu(self)
        self.credits_menu = CreditMenu(self)
        self.current_menu = self.main_menu
        self.player = Player()
        self.levels = [Level0(self)]
        self.current_level_index = 0
        self.current_level = self.levels[self.current_level_index]
        self.player.position.x = self.current_level.startx
        self.player.position.y = self.current_level.starty
        print(f"Position initiale du joueur : x={self.player.position.x}, y={self.player.position.y}")
        self.backgrounds = [
            pygame.image.load(f"./assets/Clouds/Clouds_1/{i}.png").convert_alpha()
            for i in range(1, 5, 1)
        ]
        self.backgrounds = [pygame.transform.scale(bg, (self.WINDOW_W, self.WINDOW_H)) for bg in self.backgrounds]

        self.nightybg = [
            pygame.image.load(f"./assets/Clouds/Clouds_1/{i}.png").convert_alpha()
            for i in range(1, 5, 1)
        ]
        self.nightybg = [pygame.transform.scale(bg, (self.WINDOW_W, self.WINDOW_H)) for bg in self.nightybg]

        self.dawnbg = [
            pygame.image.load(f"./assets/Clouds/Clouds_1/{i}.png").convert_alpha()
            for i in range(1, 5, 1)
        ]
        self.dawnbg = [pygame.transform.scale(bg, (self.WINDOW_W, self.WINDOW_H)) for bg in self.dawnbg]

    def game_loop(self):
        self.reset_clock()
        while self.playing:
            dt = self.clock.tick(60) * .001 * 60
            self.check_event()
            if self.ESC_KEY:
                self.playing = False
            self.player.update(dt)
            self.display.fill((0, 0, 0))
            for bg in self.backgrounds:
                self.display.blit(bg, (0,0))
            self.current_level.draw()
            self.player.draw(self.display)
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
                    self.player.reset_key()

            #Player event 
                if event.key == pygame.K_LEFT:
                    self.player.LEFT_KEY, self.player.FACING_LEFT = True, True
                elif event.key == pygame.K_RIGHT:
                    self.player.RIGHT_KEY, self.player.FACING_LEFT = True, False
                elif event.key == pygame.K_SPACE:
                    self.player.jump()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.LEFT_KEY = False
                elif event.key == pygame.K_RIGHT:
                    self.player.RIGHT_KEY = False
                elif event.key == pygame.K_SPACE:
                    if self.player.is_jumping:
                        self.player.velocity.y *= 0.25
                        self.player.is_jumping = False


    def reset_key(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESC_KEY = False, False, False, False, False

    def draw_text(self, text, size, x, y, color, line_spacing = 10):
        font = pygame.font.Font(self.font_name, size)
        lines = text.split("\n")
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, color)
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y + i * (size + line_spacing))
            self.display.blit(text_surface, text_rect)

    def next_level(self):
        if self.current_level_index < len(self.levels) - 1:
            self.current_level_index += 1
            self.current_level = self.levels[self.current_level_index]
        else:
            self.playing = False
            self.current_menu = self.credits_menu

    def reset_clock(self):
        self.clock.tick()