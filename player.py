from map_reader import MapReader
from player_states import PlayerState
from typing import Tuple, Literal

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
            match current_char:
                case "-":
                    continue
                case "|":
                    continue
                case "/":
                    self.change_state(current_char)
                case "\\":
                    self.change_state(current_char)
                case '#':
                    is_over = True
                case 'EOF':
                    raise Exception("File endend unexpectedly")
                case _:
                    if current_char.isdigit():
                        self.match_num(current_char)
                    else:
                        raise Exception("Something went wrong")
            

    def sum_money(self) -> int:
        return sum(self.money_arr)  
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

    def add_money(self, money: int):
        self.money_arr.append(money)

    def consume_char(self) -> str:
        self.advance()
        return self.map.get_pos(self.pos_x, self.pos_y)

    def match_num(self, first_num: str):
        # -pedro123outra
        current_num = first_num
        next_char = self.peek()
        while next_char.isdigit():
            self.advance()
            current_num += next_char
            next_char = self.peek()

        self.add_money(int(current_num))

    def peek(self):
        next_x = self.pos_x
        next_y = self.pos_y
        match self.state:
            case PlayerState.RIGHT:
                next_x += 1 
            case PlayerState.LEFT:
                next_x += - 1 
            case PlayerState.DOWN:
                next_y += + 1
            case PlayerState.UP:
                next_y += - 1

        return self.map.get_pos(next_x, next_y)
    
    def change_state(self, c: Literal["/", "\\"]):
        match(c):
            case '/':
                match self.state:
                    case PlayerState.RIGHT:
                        self.state = PlayerState.UP
                    case PlayerState.LEFT:
                        self.state = PlayerState.DOWN
                    case PlayerState.DOWN:
                        self.state = PlayerState.LEFT
                    case PlayerState.UP:
                        self.state = PlayerState.RIGHT
            case '\\':
                match self.state:
                    case PlayerState.RIGHT:
                        self.state = PlayerState.DOWN
                    case PlayerState.LEFT:
                        self.state = PlayerState.UP
                    case PlayerState.DOWN:
                        self.state = PlayerState.RIGHT
                    case PlayerState.UP:
                        self.state = PlayerState.LEFT