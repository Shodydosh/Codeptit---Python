def cal(n):
    if(n <= 50): return n * 102
    elif(n <= 100):
        return (n-50) * 150 * 1.03 + 50 * 103
    else:
        return ((50) * 100 + (50) * 150 + (n-100) * 200) * 1.05
class Customer:
    def __init__(self, stt, name, new, old):
        if(stt < 10): self.stt = "KH0" + str(stt)
        else: self.stt = "KH" + str(stt)
        self.name = name
        self.invoice = cal(old-new)

customers = []
for i in range(int(input())):
    a = input()
    b = int(input())
    c = int(input())
    CUS = Customer(i+1, a, b, c)
    customers.append(CUS)

customers_sorted = sorted(customers, key=lambda x : (-x.invoice))
for c in customers_sorted:
    print(c.stt, c.name, end=" ")
    print(f'%.f' % c.invoice)
