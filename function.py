#change vs code to light mode and use codesnap extension

class Student:
    """
    Represents a student with a list of scores and methods to add scores and calculate grades.
    """

    def __init__(self):
        """
        Initializes a new Student object with an empty list of scores.
        """
        self.scores = []

    def add_score(self, score):
        """
        Adds a score to the student's list of scores.

        Args:
            score (int): The score to be added.
        """
        self.scores.append(score)

    def calculate_grade(self):
        """
        Calculates the average score and corresponding grade for the student.

        Returns:
            tuple: A tuple containing the average score and the corresponding grade.
        """
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
    """
    Manages a collection of students and provides methods to add students, add scores, and calculate
    grades.
    """

    def __init__(self):
        """
        Initializes a new GradeMaster object with an empty dictionary to store students.
        """
        self.grade_dict = {}

    def add_student(self, student_name):
        """
        Adds a new student to the GradeMaster's collection.

        Args:
            student_name (str): The name of the student to be added.
        """
        self.grade_dict[student_name] = Student()

    def student_exists(self, student_name):
        """
        Checks if a student with the given name exists in the GradeMaster's collection.

        Args:
            student_name (str): The name of the student to check.

        Returns:
            bool: True if the student exists, False otherwise.
        """
        return student_name in self.grade_dict

    def add_score(self, student_name, score):
        """
        Adds a score to the specified student's list of scores.

        Args:
            student_name (str): The name of the student.
            score (int): The score to be added.
        """
        student = self.grade_dict[student_name]
        student.add_score(score)

    def calculate_grade(self, student_name):
        """
        Calculates the average score and corresponding grade for the specified student.

        Args:
            student_name (str): The name of the student.

        Returns:
            tuple: A tuple containing the average score and the corresponding grade.
        """
        student = self.grade_dict[student_name]
        return student.calculate_grade()


def get_option():
    """
    Prompts the user to choose an option and returns the selected option.

    Returns:
        int: The selected option.
    """
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
    """
    Prompts the user to enter a student name and returns the entered name.

    Returns:
        str: The entered student name.
    """
    name = input("Please enter the student name: ")
    return name.strip().capitalize()


def get_test_score(student_name):
    """
    Prompts the user to enter a test score for the specified student and returns the entered score.

    Args:
        student_name (str): The name of the student.

    Returns:
        int: The entered test score.
    """
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
    """
    Prompts the user to enter a new student name and returns the entered name.

    Args:
        grade_master (GradeMaster): The GradeMaster object.

    Returns:
        str: The entered student name.
    """
    while True:
        name = get_student_name()
        if grade_master.student_exists(name):
            print("Student already exists. Please try again.")
        else:
            return name


def get_existing_student_name(grade_master):
    """
    Prompts the user to enter an existing student name and returns the entered name.

    Args:
        grade_master (GradeMaster): The GradeMaster object.

    Returns:
        str: The entered student name.
    """
    while True:
        name = get_student_name()
        if not grade_master.student_exists(name):
            print("Student is not in the class. Please try again.")
        else:
            return name


def main():
    """
    The main function that runs the Grade Master program.
    """
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
