import sys
from game_engine import *
import pygame as pg
import button
from main import *
from levels_manager_displayer import *
from levels.level_1 import *
from levels.level_2 import *
from levels.level_3 import *
from levels.level_4 import *
from levels.level_5 import *
from levels.level_6 import *


class LevelsManager:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.curr_gun_chosen = main_menu.game_session.player_config.type_of_weapon
        self.should_run = True
        self.rect = pg.Rect(50, 50, 50, 50)
        self.levels_manager_displayer = LevelsManagerDisplayer(self)
        self.reset(False)

    def reset(self, should_reset_levels_music):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.NOFRAME)
        self.should_run = True
        pg.mouse.set_visible(True)
        if should_reset_levels_music:
            self.main_menu.sound.menu_bg_music.play()
        self.levels_manager_displayer.draw_main_background()
        self.levels_manager_displayer.draw_guns_background()
        self.levels_manager_displayer.draw_player_score_heading()
        self.levels_manager_displayer.draw_player_score()
        self.levels_manager_displayer.draw_pistol()
        self.levels_manager_displayer.draw_shotgun()
        self.levels_manager_displayer.draw_automat()
        self.levels_manager_displayer.draw_locks()
        self.levels_manager_displayer.draw_levels_background()
        self.levels_manager_displayer.draw_button_levels()
        self.levels_manager_displayer.draw_aim_at(self.curr_gun_chosen)

    def check_new_gun_selected(self):
        # get mouse position
        pos = pg.mouse.get_pos()
        new_gun_chosen = None
        score = self.main_menu.game_session.score
        if self.pistol_rect.collidepoint(pos) and score >= XP_TO_UNLOCK_PISTOL:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    new_gun_chosen = TypeOfWeapon.PISTOL
                    break
        if self.shotgun_rect.collidepoint(pos) and score >= XP_TO_UNLOCK_HANDGUN:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    new_gun_chosen = TypeOfWeapon.SHOTGUN
                    break
        if self.automat_rect.collidepoint(pos) and score >= XP_TO_UNLOCK_AUTOMAT:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    new_gun_chosen = TypeOfWeapon.AUTOMAT
                    break

        return new_gun_chosen

    def run(self):
        clock = pg.time.Clock()
        clicked_on_level = False
        game = {}
        while self.should_run:
            gun_chosen = self.check_new_gun_selected()
            if gun_chosen is not None and gun_chosen is not self.curr_gun_chosen:
                self.curr_gun_chosen = gun_chosen
                self.main_menu.game_session.player_config.type_of_weapon = self.curr_gun_chosen
                self.reset(False)

            if self.level_1_btn.update_state(self.screen, self.should_run):
                game = Game(self, LevelConfig(Level1()))
                clicked_on_level = True
            if self.level_2_btn.update_state(self.screen, self.should_run):
                game = Game(self, LevelConfig(Level2()))
                clicked_on_level = True
            if self.level_3_btn.update_state(self.screen, self.should_run):
                game = Game(self, LevelConfig(Level3()))
                clicked_on_level = True
            if self.level_4_btn.update_state(self.screen, self.should_run):
                game = Game(self, LevelConfig(Level4()))
                clicked_on_level = True
            if self.level_5_btn.update_state(self.screen, self.should_run):
                game = Game(self, LevelConfig(Level5()))
                clicked_on_level = True
            if self.level_6_btn.update_state(self.screen, self.should_run):
                game = Game(self, LevelConfig(Level6()))
                clicked_on_level = True
            if self.back_button.update_state(self.screen, self.should_run):
                self.main_menu.reset(False)
                self.should_run = False
            if clicked_on_level:
                break

            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()

            pg.display.update()

        if clicked_on_level:
            self.main_menu.sound.menu_bg_music.stop()
            game.run()
            self.should_run = False
