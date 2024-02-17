import sys
from game_engine import *
import pygame as pg
import button
from main import *
from levels.level_1 import *
from levels.level_2 import *
from levels.level_3 import *
from levels.level_4 import *
from levels.level_5 import *
from levels.level_6 import *


class LevelsManagerDisplayer:
    def __init__(self, levels_manager):
        self.levels_manager = levels_manager

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def render_text(self, text, position):
        # Render text onto a surface
        text_surface = pg.font.SysFont('Arial', 40).render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(topleft=position)

        self.levels_manager.screen.blit(text_surface, text_rect)

    def draw_main_background(self):
        background_image = pg.image.load('resources/levels_bg.jpeg')
        background_image = pg.transform.scale(background_image, (WIDTH, HEIGHT))
        background_rect = background_image.get_rect()
        self.levels_manager.screen.blit(background_image, background_rect)

    def draw_guns_background(self):
        guns_background_image = pg.image.load('resources/gun_bg.png')
        guns_background_image = pg.transform.scale(guns_background_image, (400, 700))
        guns_background_rect = guns_background_image.get_rect()
        guns_background_rect.x += 1130
        guns_background_rect.y += 90
        transparent_image = guns_background_image.convert_alpha()
        transparent_image.fill((255, 255, 255, 230), None, pg.BLEND_RGBA_MULT)
        self.levels_manager.screen.blit(transparent_image, guns_background_rect)

    def draw_player_score_heading(self):
        self.render_text("Score:", (1280, 120))

    def draw_player_score(self):
        digit_size = 50
        digit_images = [self.get_texture(f'resources/textures/digits/{i}.png', [digit_size] * 2)
                        for i in range(11)]
        digits = dict(zip(map(str, range(11)), digit_images))
        score = str(self.levels_manager.main_menu.game_session.score)
        x_offset = (150 - digit_size * len(score)) / 2
        for i, char in enumerate(score):
            image = digits[char]
            image_rect = image.get_rect(topleft=(i * digit_size + 1250 + x_offset, 190))
            self.levels_manager.screen.blit(image, image_rect)
        image = pg.image.load('resources/xp.png')
        image_rect = image.get_rect(topleft=((i + 1) * digit_size + 1250 + x_offset, 220))
        image = pg.transform.scale(image, (30, 30))
        self.levels_manager.screen.blit(image, image_rect)

    def draw_pistol(self):
        pistol_image = pg.image.load('resources/gun_bg/pistol.png')
        pistol_image = pg.transform.scale(pistol_image, (160, 160))
        self.levels_manager.pistol_rect = pistol_image.get_rect()
        self.levels_manager.pistol_rect.x += 1260
        self.levels_manager.pistol_rect.y += 260
        transparent_image_pistol = pistol_image.convert_alpha()
        transparent_image_pistol.fill((255, 255, 255, 210), None, pg.BLEND_RGBA_MULT)
        self.levels_manager.screen.blit(transparent_image_pistol, self.levels_manager.pistol_rect)

    def draw_shotgun(self):
        shotgun_image = pg.image.load('resources/gun_bg/shotgun.png')
        shotgun_image = pg.transform.scale(shotgun_image, (245, 275))
        self.levels_manager.shotgun_rect = shotgun_image.get_rect()
        self.levels_manager.shotgun_rect.x += 1230
        self.levels_manager.shotgun_rect.y += 370
        transparent_image_shotgun = shotgun_image.convert_alpha()
        transparent_image_shotgun.fill((255, 255, 255, 210), None, pg.BLEND_RGBA_MULT)
        self.levels_manager.screen.blit(transparent_image_shotgun, self.levels_manager.shotgun_rect)

    def draw_automat(self):
        automat_image = pg.image.load('resources/gun_bg/gun.png')
        automat_image = pg.transform.scale(automat_image, (360, 260))
        self.levels_manager.automat_rect = automat_image.get_rect()
        self.levels_manager.automat_rect.x += 1140
        self.levels_manager.automat_rect.y += 580
        transparent_image_automat = automat_image.convert_alpha()
        transparent_image_automat.fill((255, 255, 255, 210), None, pg.BLEND_RGBA_MULT)
        self.levels_manager.screen.blit(transparent_image_automat, self.levels_manager.automat_rect)

    def draw_lock(self, x, y):
        automat_image = pg.image.load('resources/gun_bg/lock2.png')
        automat_image = pg.transform.scale(automat_image, (80, 80))
        automat_rect = automat_image.get_rect()
        automat_rect.x += x
        automat_rect.y += y
        transparent_image_automat = automat_image.convert_alpha()
        transparent_image_automat.fill((255, 255, 255, 240), None, pg.BLEND_RGBA_MULT)
        self.levels_manager.screen.blit(transparent_image_automat, automat_rect)

    def draw_locks(self):
        score = self.levels_manager.main_menu.game_session.score
        offset = 80
        if score < XP_TO_UNLOCK_PISTOL:
            self.draw_lock(1260 + offset - 40, 260 + offset - 40)
        if score < XP_TO_UNLOCK_HANDGUN:
            self.draw_lock(1230 + offset - 10, 370 + offset - 10)
        if score < XP_TO_UNLOCK_AUTOMAT:
            self.draw_lock(1140 + offset + 80, 580 + offset)

    def draw_aim_at(self, type_of_gun):
        x, y = 0, 0
        if type_of_gun == TypeOfWeapon.PISTOL:
            x = 1230
            y = 240
        elif type_of_gun == TypeOfWeapon.SHOTGUN:
            x = 1230
            y = 385
        elif type_of_gun == TypeOfWeapon.AUTOMAT:
            x = 1230
            y = 590

        x_offset = 100
        y_offset = 50
        aim_image = pg.image.load('resources/gun_bg/arrow.png')
        aim_image = pg.transform.scale(aim_image, (70, 70))
        aim_rect = aim_image.get_rect()
        aim_rect.x += x - x_offset
        aim_rect.y += y + y_offset
        transparent_image_aim = aim_image.convert_alpha()
        transparent_image_aim.fill((255, 255, 255, 240), None, pg.BLEND_RGBA_MULT)
        self.levels_manager.screen.blit(transparent_image_aim, aim_rect)

    def draw_levels_background(self):
        levels_background_image = pg.image.load('resources/levels_digits_bg.png')
        levels_background_image = pg.transform.scale(levels_background_image, (800, 700))
        levels_background_rect = levels_background_image.get_rect()
        levels_background_rect.x += 290
        levels_background_rect.y += 100
        transparent_image = levels_background_image.convert_alpha()
        transparent_image.fill((255, 255, 255, 210), None, pg.BLEND_RGBA_MULT)
        self.levels_manager.screen.blit(transparent_image, levels_background_rect)

    def draw_button_levels(self):
        # images
        level_1_img = pg.image.load('resources/textures/digits/1.png').convert_alpha()
        level_2_img = pg.image.load('resources/textures/digits/2.png').convert_alpha()
        level_3_img = pg.image.load('resources/textures/digits/3.png').convert_alpha()
        level_4_img = pg.image.load('resources/textures/digits/4.png').convert_alpha()
        level_5_img = pg.image.load('resources/textures/digits/5.png').convert_alpha()
        level_6_img = pg.image.load('resources/textures/digits/6.png').convert_alpha()
        back_game_img = pg.image.load('resources/buttons/back.png').convert_alpha()
        # buttons
        self.levels_manager.level_1_btn = button.Button(410, 170, level_1_img, 2)
        self.levels_manager.level_2_btn = button.Button(410, 370, level_2_img, 2)
        self.levels_manager.level_3_btn = button.Button(410, 570, level_3_img, 2)
        self.levels_manager.level_4_btn = button.Button(790, 170, level_4_img, 2)
        self.levels_manager.level_5_btn = button.Button(790, 370, level_5_img, 2)
        self.levels_manager.level_6_btn = button.Button(790, 570, level_6_img, 2)
        self.levels_manager.back_button = button.Button(80, 670, back_game_img, 0.33)
