print("""Please choose one of the following: 
                        1. Add a student to your class
                        2. Add a test grade for a student
                        3. Calculate the student's overall grade""")
while True:
        decision = input("Enter 1, 2, or 3: ")
        if decision in ("1", "2", "3"):
            break
        else:
            print("Invalid input. Please enter options 1, 2, or 3.")

if decision == "1":
     print("Add a student to your class.")
     classdict = {}
     studentname = input("Please enter the name of the student: ")
     classdict[studentname] = []
     while True:
          morestudents = input("Would you like to add another student (yes/no): ").lower()
          if morestudents in ("yes", "no"):
               break
          else:
               print("Invalid input. Please enter 'Yes' or 'No'.")
elif decision == "2":
     print("2")
else:
     print("3")
