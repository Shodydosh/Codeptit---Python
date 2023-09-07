import math
from decimal import ROUND_HALF_UP, Decimal

class Student: 
    def __init__(self, stt, name, data):
        if(stt < 10): self.stt = "HS0" + str(stt)
        else: self.stt = "HS" + str(stt)

        x = 2 * data[0] + 2 * data[1]
        for i in range(2, 10) :
            x += data[i]
        x /= 12
        if x < 5 : self.xepLoai = 'YEU'
        elif x < 7 : self.xepLoai = 'TB'
        elif x < 8 : self.xepLoai = 'KHA'
        elif x < 9 : self.xepLoai = 'GIOI'
        else : self.xepLoai = 'XUAT SAC'
        self.tb = x.quantize(Decimal('0.1'), ROUND_HALF_UP)
        self.name = name

    def output(self):
        print(self.stt, self.name, self.tb, self.xepLoai)
    
students = []
for i in range(int(input())):
    name = input()
    data = [Decimal(x) for x in input().split()]
    S = Student(i+1, name, data)
    students.append(S)

sorted_students = sorted(students, key=lambda x : (-x.tb, x.stt))
for s in sorted_students:
    s.output()
