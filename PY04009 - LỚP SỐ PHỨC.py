import math

class ComplexNum:
    def __init__(self, x, y,):
        self.x = x
        self.y = y

    def calC(self, other):
        a = self.x + other.x
        b = self.y + other.y
        resX = a * self.x - b * self.y
        resY = self.y * a + self.x * b
        return resX, resY

    def calD(self, other):
        a = self.x + other.x
        b = self.y + other.y
        resX = a * a - b * b
        resY = b * a + a * b
        return resX, resY

for _ in range(int(input())):
    a = list(map(int, input().split()))
    A = ComplexNum(a[0], a[1])
    B = ComplexNum(a[2], a[3])
    tmpC = A.calC(B)
    tmpD = A.calD(B)
    print(f'{tmpC[0]}', end = "")
    if tmpC[1] < 0:
        print(f' - {-tmpC[1]}i, ', end = "")
    else:
        print(f' + {tmpC[1]}i, ', end = "")

    print(f'{tmpD[0]}', end = "")
    if tmpD[1] < 0:
        print(f' - {-tmpD[1]}i')
    else:
        print(f' + {tmpD[1]}i')
