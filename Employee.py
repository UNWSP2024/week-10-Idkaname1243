# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.

class Employee:
    def __init__(self, name, idnumber, department, jobtitle):
        self.__name = name
        self.__idnumber = idnumber
        self.__department = department
        self.__jobtitle = jobtitle

    def save_to_file(self):
        entry = f"{self.__name}\t{self.__idnumber}\t{self.__department}\t{self.__jobtitle}\n"
        with open('employees.txt', 'r') as file:
            lines = file.readlines()
            if entry in lines:
                print(f"Duplicate entry for {self.__name} - skipping save.")
                return
        with open('employees.txt', 'a') as file:
            file.write(entry)
    def display(self):
        print(f"Name: {self.__name}")
        print(f"ID Number: {self.__idnumber}")
        print(f"Department: {self.__department}")
        print(f"Job Title: {self.__jobtitle}")
        print("-" * 30)


def create_employee():
    name = input("Enter the name of the employee: ")
    idnumber = input("Enter the ID number of the employee: ")
    department = input("Enter the department of the employee: ")
    jobtitle = input("Enter the job title of the employee: ")
    employee = Employee(name, idnumber, department, jobtitle)
    employee.save_to_file()
    employee.display()

def startline():
    with open('employees.txt', 'r') as file:
        lines = file.readlines()
    if not lines:
        lines = ['Name\tID Number\tDepartment\tJob Title\n']
    elif lines[0].strip() != 'Name\tID Number\tDepartment\tJob Title':
        lines[0] = 'Name\tID Number\tDepartment\tJob Title\n'
    with open('employees.txt', 'w') as file:
        file.writelines(lines)

sm = Employee('Susan Meyers',47899, 'Accounting','Vice President')
mj = Employee('Mark Jones',39119,'IT','Programmer')
jr = Employee('Joy Rogers',81774,'Manufacturing','Engineer')
startline()
sm.save_to_file()
mj.save_to_file()
jr.save_to_file()
for _ in range(3):
    create_employee()
