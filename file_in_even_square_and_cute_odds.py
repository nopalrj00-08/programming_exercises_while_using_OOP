class Seperator:
    def __init__(self, even_squares, odds_cubes, integers_file):
        self.even_squares = even_squares
        self.odds_cubes = odds_cubes
        self.integers_file = integers_file
    def prepare_file(self):
        with open(self.integers_file, "w") as int_file:
            for integer in range(1,21):
                int_file.write(f"{integer}\n")
    def main_calculation(self):
        with open(self.integers_file, "r") as my_file:
            numbers = [int(line.strip()) for line in my_file if line.strip()]
        with open(self.even_squares, "r") as even_squares_file:
            for num in numbers:






