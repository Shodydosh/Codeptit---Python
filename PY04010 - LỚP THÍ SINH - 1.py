import math
class Student: 
    def __init__(self, name, dob, m1, m2, m3):
        self.name = name
        self.dob = dob
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def cal(self):
        return self.m1+self.m2+self.m3
    
name = input()
dob = input()
m1 = float(input())
m2 = float(input())
m3 = float(input())
S = Student(name, dob, m1, m2, m3)
print(S.name, S.dob, end =" ")
print("%.1f" % S.cal())
