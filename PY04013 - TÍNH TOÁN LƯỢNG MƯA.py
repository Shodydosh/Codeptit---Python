class Rain:
    def __init__(self, name, sTime, eTime, amount):
        self.name = name
        self.sTime = sTime
        self.eTime = eTime
        self.amount = amount
        
Amount = {}
Time = {}

def toMin(s):
    a, b = list(map(int, s.split(':')))
    return a*60+b

for _ in range(int(input())):
    a = input()
    b = input()
    c = input()
    d = int(input())
    R = Rain(a, b, c, d)
    toMin(b)
    if a not in Amount:
        Amount[a] = d
        tmp = toMin(c) - toMin(b)
        Time[a] = tmp
    else:
        Amount[a] += d
        Time[a] += (toMin(c) - toMin(b))

stt = 1
for key, value in Amount.items():
    if stt < 10: print("T0", end=str(stt))
    else: print("T", end=str(stt))
    print(end=" ")
    stt += 1

    t = Time[key]
    amount = value
    print(key, end = ' ')
    print(f'%.2f' % (int(amount) / (t / 60)))
