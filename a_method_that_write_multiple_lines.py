class Writer:
    def __init__(self,writer_file):
            self.writer_file = writer_file
    def main_file(self):
        try:
            data_lines = []
            while True:
                lines_data = input("Enter line: ")
                data_lines.append(lines_data)
                choice_input = input("Are there more lines y/n?")
                if choice_input != "y":
                    break
            with open(self.writer_file,'w') as writer_data:
                for line in data_lines:
                    writer_data.write(line + "\n")
        except FileNotFoundError:
            print("File not found")
        except PermissionError:
            print("Permission error")
        except ValueError:
            print("Value error")
if __name__ == "__main__":
    writer = Writer("writer.txt")
    writer.main_file()

