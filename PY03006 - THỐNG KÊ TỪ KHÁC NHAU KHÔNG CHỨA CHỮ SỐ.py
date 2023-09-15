import re
words = []
t = int(input())
for _ in range(t):
    text = input()
    cleaned_text = re.sub(r'\d', '', text).lower() # this will find number and replace with ''
    words += re.findall(r'\b\w+\b', cleaned_text)
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
    print(a["w"], a["f"])
