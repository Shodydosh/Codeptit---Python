class NhanVien :
    def __init__(self, id, ten, d1, d2) :
        self.id = 'TS0' + str(id)
        self.ten = ten
        if d1 > 10 : d1 /= 10
        if d2 > 10 : d2 /= 10
        self.d = (d1 + d2) / 2
        if self.d < 5 : self.l = 'TRUOT'
        elif self.d < 8 : self.l = 'CAN NHAC'
        elif self.d < 9.5 : self.l = 'DAT'
        else : self.l = 'XUAT SAC'
    
n = int(input())
a = []
for i in range(n) :
    ten = input()
    d1 = float(input()) 
    d2 = float(input())
    a.append(NhanVien(i + 1, ten, d1, d2))
a.sort(key = lambda x : x.d, reverse = True)
for i in a :
    print(i.id, i.ten, '{:.2f}'.format(i.d), i.l)

