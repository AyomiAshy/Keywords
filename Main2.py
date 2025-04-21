students=int(input("Enter the number of students in the class:"))
for i in range(students):
    name=input(f"Enter the name of the student {i+1}:")
    if name=="":
        pass
    else:
        print(f"Student {i+1}:{name}")