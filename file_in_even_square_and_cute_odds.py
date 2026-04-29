from six import integer_types


class Seperator:
    def __init__(self, even_squares, odds_cubes, integers_file):
        self.even_squares = even_squares
        self.odds_cubes = odds_cubes
        self.integers_file = integers_file
    def prepare_file(self):
        try:
            with open(self.integers_file, "w") as int_file:
                for integer in range(1,21):
                    int_file.write(f"{integer}\n")
    def square_calculation(self):
        with open(self.integers_file, "r") as even_file:
            numbers = [int(line.strip()) for line in even_file if line.strip()]
        with open(self.even_squares, "r") as even_squares_file:
            for num in numbers:
                if num % 2 == 0:
                    even_squares_file.write(f"{num**2}\n")
    def cube_calculation(self):
        with open(self.integers_file, "r") as odd_file:
            numbers = [int(line.strip()) for line in odd_file if line.strip()]
        with open(self.odds_cubes, "r") as cube_file:
            for num in numbers:
                if num % 2 == 0:
                    cube_file.write(f"{num**3}\n")






