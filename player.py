from map_reader import MapReader
from player_states import PlayerState
from typing import Tuple

class Player:

    def __init__(self, map: MapReader) -> None:
        self.map: MapReader = map
        self.pos_x, self.pos_y = map.get_start_pos()
        self.state: PlayerState = PlayerState.RIGHT
        self.money_arr: list[int] = []

    
    def run(self):
        is_over = False

        while not is_over:
            current_char = self.consume_char()
            print(current_char)
            if current_char == "EOF":
                is_over = True
                
    def advance(self):
        match self.state:
            case PlayerState.RIGHT:
                self.pos_x += 1 
            case PlayerState.LEFT:
                self.pos_x+= -1
            case PlayerState.DOWN:
                self.pos_y += 1
            case PlayerState.UP:
                self.pos_y += -1
    
    def consume_char(self) -> str:
        self.advance()
        return self.map.get_pos(self.pos_x, self.pos_y)

