import sys

import button
from map import *
from player import *
from raycasting import *
from object_renderer import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *
from enums import *
from level_config import *
from player_config import *


class Game:
    def __init__(self, levels_menu, level_config):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.NOFRAME)
        self.level_config = level_config
        self.levels_menu = levels_menu
        self.new_game(level_config)
        self.sound = Sound(self)
        if self.levels_menu.main_menu.game_session.player_config.play_background_in_game_music:
            self.sound.theme.set_volume(1)
            self.sound.theme.play()
        self.should_run = True

    def render_text(self, text, position):
        # Render text onto a surface
        text_surface = pg.font.SysFont('Arial', 40).render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(topleft=position)

        # Blit the text surface onto the screen
        self.screen.blit(text_surface, text_rect)

    def display_aim(self):
        aim_image = pg.image.load('resources/gun_bg/aim.png')
        aim_image = pg.transform.scale(aim_image, (50, 50))
        aim_rect = aim_image.get_rect()
        aim_rect.x += 770
        aim_rect.y += 450
        transparent_image_aim = aim_image.convert_alpha()
        transparent_image_aim.fill((255, 255, 255, 210), None, pg.BLEND_RGBA_MULT)
        self.screen.blit(transparent_image_aim, aim_rect)

    def new_game(self, level_config):
        self.map = Map(self)
        self.map.set_map(level_config.map)
        score = 0
        if hasattr(self, 'player'):
            score = self.player.score
        self.player = Player(self)
        self.player.score = score
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self, level_config)
        self.weapon = Weapon(self, self.levels_menu.main_menu.game_session.player_config.type_of_weapon)
        self.pathfinding = PathFinding(self)


    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

    def draw(self):
        self.object_renderer.draw()
        self.weapon.draw()
        for i, char in enumerate("Press [Esc] to exit..."):
            self.render_text(char, (i * 30 + 500, 10))
        self.display_aim()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.should_run = False
            elif event.type == self.global_event:
                self.global_trigger = True

            self.player.single_fire_event(event)

    def run(self):
        while self.should_run:
            self.check_events()
            self.update()
            self.draw()
        if not self.should_run:
            self.sound.theme.stop()
            self.levels_menu.reset(True)
            self.levels_menu.run()
