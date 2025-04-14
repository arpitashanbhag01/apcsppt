class Student:


    def __init__(self):

        self.scores = []

    def add_score(self, score):

        self.scores.append(score)

    def calculate_grade(self):

        total = 0
        for score in self.scores:
            total += score
        average = int(total / len(self.scores))
        if average >= 90:
            return average, "A"
        if average >= 80:
            return average, "B"
        if average >= 70:
            return average, "C"
        if average >= 60:
            return average, "D"
        else:
            return average, "F"


class GradeMaster:


    def __init__(self):

        self.grade_dict = {}

    def add_student(self, student_name):

        self.grade_dict[student_name] = Student()

    def student_exists(self, student_name):
    
        return student_name in self.grade_dict

    def add_score(self, student_name, score):
     
        student = self.grade_dict[student_name]
        student.add_score(score)

    def calculate_grade(self, student_name):
       
        student = self.grade_dict[student_name]
        return student.calculate_grade()


def get_option():

    print(
        """\nGrade Master Actions:
        1. Add a student to your class
        2. Add a test score to a student
        3. Calculate the overall grade of a student
        4. Exit the program\n"""
    )
    while True:
        try:
            response = int(input("Please choose one option (1, 2, 3, 4): "))
            if response not in [1, 2, 3, 4]:
                print("Please enter a valid response")
            else:
                return response
        except ValueError:
            print("Please enter a valid response")


def get_student_name():

    name = input("Please enter the student name: ")
    return name.strip().capitalize()


def get_test_score(student_name):

    while True:
        try:
            test_score = int(input("Please enter " + student_name + "'s test score: "))
            if test_score not in range(1, 100):
                print("Please enter a valid test score.")
            else:
                return test_score
        except ValueError:
            print("Please enter a valid test score.")


def get_new_student_name(grade_master):
   
    while True:
        name = get_student_name()
        if grade_master.student_exists(name):
            print("Student already exists. Please try again.")
        else:
            return name


def get_existing_student_name(grade_master):
  
    while True:
        name = get_student_name()
        if not grade_master.student_exists(name):
            print("Student is not in the class. Please try again.")
        else:
            return name


def main():

    grade_master = GradeMaster()

    while True:
        option = get_option()
        if option == 1:
            name = get_new_student_name(grade_master)
            grade_master.add_student(name)
        elif option == 2:
            name = get_existing_student_name(grade_master)
            score = get_test_score(name)
            grade_master.add_score(name, score)
        elif option == 3:
            name = get_existing_student_name(grade_master)
            average_score, grade = grade_master.calculate_grade(name)
            print(name + "'s grade: " + str(average_score) + "% (" + grade + ")")
        elif option == 4:
            break


if __name__ == "__main__":
    main()
