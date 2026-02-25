#Parent class 1

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        

    def display_person(self):
            print(f"Name:{self.name}")
            print(f"Age:{self.age}")

#Parent class2
class Employee:
    def __init__(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary

    def display_employee(self):
        print(f"Employee ID:{self.emp_id}")
        print(f"Salary:Rs{self.salary}")

#Child class inheriting from Person and Employeee
class Manager(Person, Employee):
    def __init__(self, name , age , emp_id, salary , department):
        #Initialize parent classes
        Person.__init__(self,name,age)
        Employee.__init__(self,emp_id,salary)


        #Manager-sspecific attribute
        self.department = department

#Manager-specific method
    def display_manager(self):
        print ("\n---Manager Details ---")
        self.display_person()
        self.display_employee()
        print(f"Department:{self.department}")


    def conduct_meeting(self):
        print(f"{self.name}is conducting a meeting for the {self.department}")


#Creating object of Manager class
manager1=Manager("ABC",35,"1000",9500,"IT")
manager1.display_manager()
manager1.conduct_meeting()


                      



