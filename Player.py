from map_reader import MapReader
from player_states import PlayerState


class Player:

    def __init__(self, map: MapReader) -> None:
        self.map = map
        self.pos_x, self.pos_y = map.get_start_pos()
        self.state = PlayerState.RIGHT
