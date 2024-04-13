from map_reader import MapReader
from player import Player
from time import perf_counter

def main():
    game_map = MapReader("casos-cohen-noite/casoG100.txt")
    player = Player(game_map)
    start_time = perf_counter()
    player.run()
    final_time = perf_counter()
    total_time = final_time - start_time
    print("Game over")
    print(f"Total money: {player.sum_money()}")
    print(f"Total time: {total_time}")
    

main()
