with(open("number.txt","r")) as my_file:
    numbers = [int(line.strip()) for line in my_file if line.strip()]
