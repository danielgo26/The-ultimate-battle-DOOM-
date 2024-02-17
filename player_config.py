from enums import *
from settings import *


class PlayerConfig:
    def __init__(self, type_of_weapon):
        self.type_of_weapon = type_of_weapon
        self.play_background_menu_music = True
        self.play_background_in_game_music = True
        self.mouse_sensitivity = MOUSE_SENSITIVITY

