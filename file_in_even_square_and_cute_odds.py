from six import integer_types


class Seperator:
    def __init__(self, even_squares, odds_cubes, integers_file):
        self.even_squares = even_squares
        self.odds_cubes = odds_cubes
        self.integers_file = integers_file
    try:
        def prepare_file(self):
            with open(self.integers_file, "w") as int_file:
                for integer in range(1,21):
                    int_file.write(f"{integer}\n")
        def square_calculation(self):
            with open(self.integers_file, "r") as even_file:
                numbers = [int(line.strip()) for line in even_file if line.strip()]
            with open(self.even_squares, "w") as even_squares_file, open(self.odds_cubes, "w") as odds_cubes_file:
                for num in numbers:
                    if num % 2 == 0:
                        even_squares_file.write(f"{num**2}\n")
                    else:
                        odds_cubes_file.write(f"{num**3}\n")
        print("Processing complete: even_output.txt and odd_output.txt files have been created.")
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("those are not integers.")
if __name__ == "__main__":
    number_seperator = Seperator("double.txt", "triple.txt", "integers.txt")
    number_seperator.prepare_file()
    number_seperator.square_calculation()






