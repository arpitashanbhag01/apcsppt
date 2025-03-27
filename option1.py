classdict = {}
adding = input("")
while adding != "No":
    studentname = input("Please enter the name of the student: ")
    adding = input("Would you like to add another student to your class (yes/no): ").capitalize()
    classdict[studentname] = []
print(classdict)
