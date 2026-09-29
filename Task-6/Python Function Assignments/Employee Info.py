'''3.	Write a function employee(**args) that accepts employee information such as
 name, ID, department and salary, then displays the information.'''

def employee(**args):
    for key, value in args.items():
        print(key, ":", value)


name = input("Enter name: ")
ID = int(input("Enter ID: "))
department = input("Enter department: ")
salary = int(input("Enter salary: "))

employee(
    name=name,
    ID=ID,
    department=department,
    salary=salary
)