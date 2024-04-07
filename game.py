from map_reader import MapReader
from player import Player

def main():
    game_map = MapReader("casos-cohen-noite/casoG100.txt")
    player = Player(game_map)

    player.run()

main()
