from settings_menu import *
from levels_manager import *
from player_config import *
from game_session import *
from levels_manager import *
import levels_manager


class StartUp:
    def __init__(self):
        pg.init()
        self.sound = Sound(self)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.NOFRAME)
        self.game_session = GameSesion(PlayerConfig(TypeOfWeapon.PISTOL), PLAYER_SCORE_INITIAL)
        self.already_playing_music = True
        self.reset(True)

    def reset(self, should_reset_menu_music):
        # general
        pg.mouse.set_visible(True)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.NOFRAME)
        if should_reset_menu_music and self.game_session.player_config.play_background_menu_music:
            self.sound.menu_bg_music.set_volume(1)
            self.sound.menu_bg_music.play()
            self.already_playing_music = True
        # background
        background_image = pg.image.load('resources/background.jpg')
        background_image = pg.transform.scale(background_image, (WIDTH, HEIGHT))
        background_rect = background_image.get_rect()
        self.screen.blit(background_image, background_rect)
        # images
        start_game_img = pg.image.load('resources/buttons/start.png').convert_alpha()
        settings_game_img = pg.image.load('resources/buttons/settings.png').convert_alpha()
        quit_game_img = pg.image.load('resources/buttons/quit.png').convert_alpha()
        # buttons
        self.start_button = button.Button(128, 40, start_game_img, 0.57)
        self.settings_button = button.Button(145, 323, settings_game_img, 0.5)
        self.quit_button = button.Button(145, 580, quit_game_img, 1.35)

    def run(self):
        while True:
            if self.game_session.player_config.play_background_menu_music and not self.already_playing_music:
                self.sound.menu_bg_music.set_volume(1)
                self.sound.menu_bg_music.play()
                self.already_playing_music = True
            elif not self.game_session.player_config.play_background_menu_music and self.already_playing_music:
                self.sound.menu_bg_music.set_volume(0)
                self.sound.menu_bg_music.play()
                self.already_playing_music = False

            if self.start_button.update_state(self.screen):
                levels = LevelsManager(self)
                levels.run()
            if self.settings_button.update_state(self.screen):
                settings = SettingsMenu(self)
                settings.run()
            if self.quit_button.update_state(self.screen):
                pg.quit()
                sys.exit()

            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()

            pg.display.update()

if __name__ == '__main__':
    startUp = StartUp()
    startUp.run()
