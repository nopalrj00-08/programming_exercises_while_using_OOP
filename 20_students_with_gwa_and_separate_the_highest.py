class Separate:
    def __init__(self,students_file):
        self.students_file = students_file
    def find_highest_gwa(self):
        highest_student = None
        highest_gwa = 1.0
        try:
            with open(self.students_file,'r') as student_file:
                for line in student_file:
                    line = line.strip()
                    parts = line.split()
                    name = parts[0]
                    gwa = float(parts[1])

                    if highest_gwa >= gwa:
                        highest_gwa = gwa
                        highest_student = name
            if highest_student:
                print(f"{highest_student.capitalize()} is the highest, with the highest gwa: {highest_gwa}")
            else:
                print(f"there is no highest gwa")
        except FileNotFoundError:
            print(f"there is no {self.students_file}")
        except ValueError:
            print(f"One of the students gwa is not a number")
if __name__ == '__main__':
    seperator = Separate("students.txt")
    seperator.find_highest_gwa()


