import math

for _ in range(int(input())):
    n = int(input())
    count = {} #dict
    for i in range(n):
        num = int(input())
        if num not in count:
            count[num] = 0
        count[num] += 1
    max_count = max(count.values())
    winners = [num for num, freq in count.items() if freq == max_count]
    print(min(winners))
