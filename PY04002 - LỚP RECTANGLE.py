import math
class Rectangle:
    def __init__(self, w, h, color):
        self.w = w
        self.h = h
        self.c = color
    
    def perimeter(self):
        return 2 * (self.w + self.h)
    
    def area(self):
        return self.w * self.h
    
    def color(self):
        return self.c.title()
    
    def isValid(self):
        return self.h > 0 and self.w > 0
    
def Decimal(n):
    return float(n)

arr = input().strip().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
if r.isValid():
    print(r.perimeter(), r.area(), r.color())
else: print('INVALID')
