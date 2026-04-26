class Sorter:
    def __init__(self,numbers_file,even_output,odd_output):
        self.numbers_file = numbers_file
        self.even_output = even_output
        self.odd_output = odd_output
    def main_process(self):
        try:
            with(open(self.numbers_file,"r")) as my_file:
                numbers = [int(line.strip()) for line in my_file if line.strip()]
            with(open(self.even_output,"w")) as even_file,open(self.odd_output,"w") as odd_file:
                for num in numbers:
                    if num % 2 == 0:
                        even_file.write(f'{num}\n')
                    else:
                        odd_file.write(f'{num}\n')
            print("Processing complete: even_output.txt and odd_output.txt files have been created.")
        except FileNotFoundError:
            print(f"The file {my_file} was not found.")
        except ValueError:
            print(f"The file contains non-integer values.")
if __name__ == "__main__":
    sorter = Sorter("numbers.txt","even_output.txt","odd_output.txt")
    sorter.main_process()
    






