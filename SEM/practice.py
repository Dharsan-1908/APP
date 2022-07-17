class Student:
    avg = 0
    def __init__(self, stNo, m1, m2, m3, m4, m5):
        self.studentNum = stNo
        self.mark1, self.mark2, self.mark3, self.mark4, self.mark5 = m1,
        m2, m3, m4, m5
    def avgMark(self):
        self.avg = (self.mark1 + self.mark2 + self.mark3 + self.mark4 +
                self.mark5) / 5
def grade(self):
    if(self.avg >= 80):
        print("Distinction")
    elif(self.avg >= 65 and self.avg < 80):
        print("Merit")
    elif(self.avg >= 50 and self.avg < 65):
        print("Pass")
    else:
        print("Fail")
        
obj = Student("20202", 10, 20, 30, 40, 80)
print(obj.studentNum)
obj.grade()
