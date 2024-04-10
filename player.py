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
        dinheiro:str =''
        while not is_over:
            current_char = self.consume_char()
            if(current_char == "-" or current_char == "|"): 
                if(dinheiro != ''):
                    self.add_money(dinheiro)
                    dinheiro = ''
                pass
            elif(current_char == "/"or current_char == "\\"):
                if(dinheiro != ''):
                    self.add_money(dinheiro)
                    dinheiro = ''
                self.fix_state(current_char)
            elif(current_char == "#"):
                if(dinheiro != ''):
                    self.add_money(dinheiro)
                    dinheiro = ''
                is_over = True
            elif(current_char.isdigit):
                dinheiro += current_char

            if current_char == "EOF":
                is_over = True
        print(self.money_arr)

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

    def fix_state(self,c:str):
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
                
                
    def add_money(self,money:str = '0'):
        if(money.isnumeric and money!='0'):
            self.money_arr.append(int(money))
