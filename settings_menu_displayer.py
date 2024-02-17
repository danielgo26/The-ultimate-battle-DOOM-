import pygame as pg
import button
from button import *


class SettingsMenuDisplayer:
    def __init__(self, settings_menu):
        self.settings_menu = settings_menu

    def display_background(self):
        background_image = pg.image.load('resources/settings_bg.jpg')
        background_image = pg.transform.scale(background_image, (WIDTH, HEIGHT))
        background_rect = background_image.get_rect()
        self.settings_menu.screen.blit(background_image, background_rect)

    def display_back_btn(self):
        back_game_img = pg.image.load('resources/buttons/back.png').convert_alpha()
        self.settings_menu.back_button = button.Button(80, 670, back_game_img, 0.33)

    def display_bg_menu_music_option(self):
        self.settings_menu.is_ok_bg_menu_music = (
            self.settings_menu.main_menu.game_session.player_config.play_background_menu_music)
        self.settings_menu.render_text("Background menu music: ", (350, 100))
        self.settings_menu.bg_menu_music_img = pg.image.load('resources/buttons/box.png')
        self.settings_menu.bg_menu_music_btn = Button(930, 95, self.settings_menu.bg_menu_music_img, 0.3)
        self.settings_menu.ok_bg_menu_music = pg.image.load('resources/buttons/ok.png')
        self.settings_menu.ok_bg_menu_music = pg.transform.scale(self.settings_menu.ok_bg_menu_music, (60, 60))
        self.settings_menu.ok_bg_menu_music_rect = self.settings_menu.ok_bg_menu_music.get_rect()
        self.settings_menu.ok_bg_menu_music_rect.x += 935
        self.settings_menu.ok_bg_menu_music_rect.y += 105

    def display_in_game_menu_music_option(self):
        self.settings_menu.is_ok_bg_in_game_music = (
            self.settings_menu.main_menu.game_session.player_config.play_background_in_game_music)
        self.settings_menu.render_text("Background in game music: ", (350, 300))
        self.settings_menu.bg_in_game_music_img = pg.image.load('resources/buttons/box.png')
        self.settings_menu.bg_in_game_music_btn = Button(930, 295, self.settings_menu.bg_in_game_music_img, 0.3)
        self.settings_menu.ok_bg_in_game_music = pg.image.load('resources/buttons/ok.png')
        self.settings_menu.ok_bg_in_game_music = pg.transform.scale(self.settings_menu.ok_bg_in_game_music, (60, 60))
        self.settings_menu.ok_bg_in_game_music_rect = self.settings_menu.ok_bg_in_game_music.get_rect()
        self.settings_menu.ok_bg_in_game_music_rect.x += 935
        self.settings_menu.ok_bg_in_game_music_rect.y += 305

    def display_mouse_sensitivity(self):
        sensitivity = self.settings_menu.main_menu.game_session.player_config.mouse_sensitivity
        self.settings_menu.render_text("Mouse sensitivity: ", (350, 500))
        background_ms_image = pg.image.load('resources/levels_digits_bg.png')
        background_ms_image = pg.transform.scale(background_ms_image, (200, 80))
        background_ms_rect = background_ms_image.get_rect()
        background_ms_rect.x += 415
        background_ms_rect.y += 560
        self.settings_menu.screen.blit(background_ms_image, background_ms_rect)
        self.settings_menu.render_text("[ " + str(sensitivity) + " ]", (455, 575), 35, (255, 0, 0))
        self.settings_menu.mouse_sens_increase_img = pg.image.load('resources/buttons/up.png')
        self.settings_menu.mouse_sens_increase_btn = Button(830, 480, self.settings_menu.mouse_sens_increase_img, 0.2)
        self.settings_menu.mouse_sens_decrease_img = pg.image.load('resources/buttons/down.png')
        self.settings_menu.mouse_sens_decrease_btn = Button(1000, 480, self.settings_menu.mouse_sens_decrease_img, 0.2)
