from numpy.ma.core import append


class Writer:
    def __init__(self,writer_file):
        self.writer_file = writer_file
    def main_file(self):
        with open(self.writer_file,'w') as writer_data:
            print(f"Enter line:\033[32m{self.writer_file}\033[0m")
        data_lines = []
        while True:
            lines_data = input("Enter line:\033[32m")
            data_lines.append(lines_data)
            choice_input = input("")
