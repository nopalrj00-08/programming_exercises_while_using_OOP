def main_process(my_file):
    with(open("numbers.txt","r")) as my_file:
        numbers = [int(line.strip()) for line in my_file if line.strip()]

    with(open("even_output.txt","w")) as even_file,open("odd_output.txt","w") as odd_file:
        for num in numbers:
            if num % 2 == 0:
                even_file.write(f'{num}\n')
            else:
                odd_file.write(f'{num}\n')






