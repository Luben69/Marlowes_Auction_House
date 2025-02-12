from multiple_Inheritance.person import Person
from multiple_Inheritance.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
