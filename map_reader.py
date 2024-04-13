from typing import Tuple


class MapReader:
    def __init__(self, file_path: str):
        self.map: list[list[str]] = []
        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                sizes = lines.pop(0).split()
                for line in lines:
                    char_array = [char for char in line]
                    self.map.append(char_array)
        except FileNotFoundError:
            print("file not found")
        self.size_x: int = int(sizes[0])
        self.size_y: int = int(sizes[1])

    def get_start_pos(self) -> Tuple[int, int]:
        for i, row in enumerate(self.map):
            if row[0] == "-":
                return (0, i)
    def get_pos(self, x: int, y: int)-> str:
        if x > self.size_x or y > self.size_y:
            return "EOF"
        return self.map[y][x]

