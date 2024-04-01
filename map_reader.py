from typing import Tuple


class MapReader:
    def __init__(self, file_path: str):
        self.map: list[list[str]] = []
        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                sizes = lines.pop(0).split()
                lines
                for line in lines:
                    char_array = [char for char in line]
                    self.map.append(char_array)
        except FileNotFoundError:
            print("file not found")
        self.size_x: int = sizes[0]
        self.size_y: int = sizes[1]

    def get_start_pos(self) -> Tuple[int, int]:
        for i, row in enumerate(self.map):
            if row[0] == "-":
                return (0, i)
