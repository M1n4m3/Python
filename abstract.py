from abc import ABC,abstractmethod
class Student(ABC):
    def __init__(self):
        self.__name = "manikandan"           # public
        self.department = "CSE"   # protected
        self._marks = "101"       # private

    def display(self):
        print("Name:",self.__name)
        print("Department:", self.department)
        print("Marks:", self._marks)

# Object creation
s1 = Student()
# Accessing public member
s1.display()

