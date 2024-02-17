from main import *
from settings_menu_displayer import *


class SettingsMenu:
    def __init__(self, main_menu):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.NOFRAME)
        self.main_menu = main_menu
        self.settings_menu_displayer = SettingsMenuDisplayer(self)

        self.settings_menu_displayer.display_background()
        self.settings_menu_displayer.display_back_btn()
        self.settings_menu_displayer.display_bg_menu_music_option()
        self.settings_menu_displayer.display_in_game_menu_music_option()
        self.settings_menu_displayer.display_mouse_sensitivity()
        self.should_run = True

    def render_text(self, text, position, size=55, color=(255, 255, 255)):
        # Render text onto a surface
        text_surface = pg.font.SysFont('Arial', size).render(text, True, color)
        text_rect = text_surface.get_rect(topleft=position)

        # Blit the text surface onto the screen
        self.screen.blit(text_surface, text_rect)

    def run(self):
        while self.should_run:
            if self.bg_menu_music_btn.update_state(self.screen, self.should_run):
                self.is_ok_bg_menu_music = not self.is_ok_bg_menu_music
            if self.bg_in_game_music_btn.update_state(self.screen, self.should_run):
                self.is_ok_bg_in_game_music = not self.is_ok_bg_in_game_music
            if self.mouse_sens_increase_btn.update_state(self.screen, self.should_run):
                self.main_menu.game_session.player_config.mouse_sensitivity = (
                    float(self.main_menu.game_session.player_config.mouse_sensitivity))
                self.main_menu.game_session.player_config.mouse_sensitivity += 0.00001
                self.main_menu.game_session.player_config.mouse_sensitivity = (
                    "{:.5f}".format(self.main_menu.game_session.player_config.mouse_sensitivity))
                self.settings_menu_displayer.display_mouse_sensitivity()
            if self.mouse_sens_decrease_btn.update_state(self.screen, self.should_run):
                self.main_menu.game_session.player_config.mouse_sensitivity = (
                    float(self.main_menu.game_session.player_config.mouse_sensitivity))
                self.main_menu.game_session.player_config.mouse_sensitivity -= 0.00001
                self.main_menu.game_session.player_config.mouse_sensitivity = (
                    "{:.5f}".format(self.main_menu.game_session.player_config.mouse_sensitivity))
                if float(self.main_menu.game_session.player_config.mouse_sensitivity) <= 0:
                    self.main_menu.game_session.player_config.mouse_sensitivity = (
                        "{:.5f}".format(0.00001))
                self.settings_menu_displayer.display_mouse_sensitivity()
            if self.back_button.update_state(self.screen, self.should_run):
                self.main_menu.reset(False)
                self.should_run = False
                break

            if self.is_ok_bg_menu_music:
                self.screen.blit(self.ok_bg_menu_music, self.ok_bg_menu_music_rect)
                self.main_menu.game_session.player_config.play_background_menu_music = True
            else:
                self.main_menu.game_session.player_config.play_background_menu_music = False

            if self.is_ok_bg_in_game_music:
                self.screen.blit(self.ok_bg_in_game_music, self.ok_bg_in_game_music_rect)
                self.main_menu.game_session.player_config.play_background_in_game_music = True
            else:
                self.main_menu.game_session.player_config.play_background_in_game_music = False

            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()

            pg.display.update()
