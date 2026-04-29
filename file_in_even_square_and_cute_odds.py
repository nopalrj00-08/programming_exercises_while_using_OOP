class Seperator:
    def __init__(self, even_squares, odds_cubes, integers_file):
        self.even_squares = even_squares
        self.odds_cubes = odds_cubes
        self.integers_file = integers_file
        def prepare_file(self):
            with open(self.integers_file, "r") as int_file:
                for integer in range(1,21):
                    int_file.write(f"{integer}\n")





