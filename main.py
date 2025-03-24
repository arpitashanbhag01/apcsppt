print("Grade Calculator")
def calculatechoice():
    while True:
        print("""Please choose one of the following: 
                        1. Add a student to your class
                        2. Add a test grade for a student
                        3. Calculate the student's overall grade""")
        decision = input("Enter 1, 2, or 3: ")
        if decision in ("1", "2", "3"):
            return decision
        else:
            print("Invalid input. Please enter options 1, 2, or 3.")

def addstudent(classdict):
    studentname = input("Please enter the name of the student: ")
    classdict[studentname] = []
    while True:
        print("Would you like to add another student to your class?")
        morenames = input("Enter 'Yes' or 'No': ").lower()
        if morenames in ("yes", "no"):
            break
        else:
            print("Invalid input. Please enter either 'Yes' or 'No'.")
    if morenames == "yes":
        # address duplicate students
        studentname = input("Please enter the name of the student: ")
        classdict[studentname] = []
    else:
        calculatechoice()
        

choice = calculatechoice()
if choice == "1":
    print("Add a student to your class.")
    classdict = {}
    addstudent(classdict)

elif choice == "2":
    print("Add a test grade for a student.")
    while True:
        #print(classdict) --> classdict isn't defined
        studentname = input("Which student would you like to add a grade for?: ")

else:
    print("Calculate the student's overall grade")
