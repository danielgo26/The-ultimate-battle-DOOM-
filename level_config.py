from map import *
from levels import *


class LevelConfig:
    def __init__(self, level):
        self.level_index = level.level_index
        self.map = level.map
        self.npc_types = level.npc_types
        self.npc_choice_weights = level.npc_choice_weights
        self.count_npc = level.count_npc
        self.restricted_area_for_spawning_npc = level.restricted_area_for_spawning_npc
