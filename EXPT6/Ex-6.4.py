class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def calcAverage(self):
        result = sum(self.marks)/len(self.marks)
        return result

    def printDetails(self):
        print("Name of the student is: ", self.name)
        print("Age of the student is: ", self.age)
        print("Average marks got by the student is: ", self.calcAverage())


marks = (12, 14, 15, 17, 12)

fMarks = frozenset(marks)

s1 = Student("Vikash", 18, fMarks)

s1.printDetails()
