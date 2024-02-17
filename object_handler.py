from sprite_object import *
from nps import *
from random import choices, randrange
from levels.level_terrain_sprites import *


class ObjectHandler:
    def __init__(self, game, level_config):
        self.game = game
        self.terrain_sprites_container = LevelTerrainSpritesContainer(game)
        self.sprite_list = self.terrain_sprites_container.get_sprites_by_level_index(level_config.level_index)
        self.npc_list = []
        add_npc = self.add_npc
        self.npc_positions = {}

        self.enemies = level_config.count_npc
        self.npc_types = level_config.npc_types
        self.weights = level_config.npc_choice_weights
        self.restricted_area = level_config.restricted_area_for_spawning_npc
        self.spawn_npc()

    def spawn_npc(self):
        for i in range(self.enemies):
            npc = choices(self.npc_types, self.weights)[0]
            pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))

    def check_win(self):
        if not len(self.npc_positions):
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game(self.game.level_config)

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        if not len(self.npc_positions):
            self.check_win()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
