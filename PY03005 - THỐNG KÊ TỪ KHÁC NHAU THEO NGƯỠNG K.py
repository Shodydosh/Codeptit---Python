import re
words = []
t, k = map(int, input().split())
for _ in range(t):
    text = input()
    words += re.findall(r'\b\w+\b', text.lower())
    
dict = {}
for w in words:
    if w not in dict:
        dict[w] = 1
    else: dict[w] += 1

freq = []
for key, value in dict.items():
    freq.append({"w" : key, "f": value})

freq = sorted(freq, key = lambda x : (-x["f"], x["w"]))
for a in freq:
    if(a["f"] >= k):
        print(a["w"], a["f"])
