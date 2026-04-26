def main_process(my_file):
    try:
        with(open("numbers.txt","r")) as my_file:
            numbers = [int(line.strip()) for line in my_file if line.strip()]
        with(open("even_output.txt","w")) as even_file,open("odd_output.txt","w") as odd_file:
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






