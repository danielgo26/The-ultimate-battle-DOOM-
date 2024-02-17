from enums import *


class GameSesion:
    def __init__(self, player_config, score=0):
        self.score = score
        self.player_config = player_config
