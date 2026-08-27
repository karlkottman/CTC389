#Karl Kottman
#CTC 389
#Lab 6

student_name = ["Alex", "Betty", "Curt", "Daria", "Eric"]



print("MENU")
print("___________")

print("1. Add student to list")
print("2. Modify student name")
print("3. Remove student")

print("__________")

x = int(input("Enter the number of the option you'd like to select:"))
if (x == 1):
    for i in student_name:
        print(i)

    new = input("Enter a name to add to the list:")
    student_name.append(new)

    for i in student_name:
        print(i)

if (x == 2):
    print("0.", student_name[0])
    print("1.", student_name[1])
    print("2.", student_name[2])
    print("3.", student_name[3])
    print("4.", student_name[4])

    edit = int(input("Enter the number of the name you wish to modify:"))
    new_name = input("Enter the new name of student:")
    student_name[edit] = new_name

    for i in student_name:
        print(i)

if (x == 3):
    print("0.", student_name[0])
    print("1.", student_name[1])
    print("2.", student_name[2])
    print("3.", student_name[3])
    print("4.", student_name[4])

    remove = int(input("Enter the number of the name you wish to remove:"))
    student_name.pop(remove)

    for i in student_name:
        print(i)




