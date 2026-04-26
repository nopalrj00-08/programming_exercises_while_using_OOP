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
                    name = line.split()[0]
                    gwa = float(line.split()[1])
                    if gwa > highest_gwa:
                        highest_gwa = gwa
                        highest_student = name
        if highest_student:
            print(f"{highest_student.capitalize()} is the highest, with the highest gwa: {highest_gwa}")
        else:
            print(f"there is no highest gwa")


