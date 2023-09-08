import math

students = []
for _ in range(int(input())):
    s = input()
    c, t = map(int, input().split())
    students.append({"name": s, "c": c, "t": t})
    sorted_students = sorted(students, key=lambda x : (-x["c"], x["t"]))
for s in sorted_students:
    print(f'{s["name"]} {s["c"]} {s["t"]}')
