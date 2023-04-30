from collections import defaultdict
import json
import matplotlib.pyplot as plt

with open("result/result.json", encoding="iso-8859-1") as f:
    data = json.load(f)

colleges = defaultdict(lambda *x: 0)
interested_subjects = defaultdict(lambda *x: 0)

for i in data:
    colleges[i[1]] += 1
    for j in i[2]:
        interested_subjects[j] += 1

c = sorted(colleges.items(), key=lambda x: x[1], reverse=True)
s = sorted(interested_subjects.items(), key=lambda x: x[1], reverse=True)

with open("../data/t25.txt") as f:
    t25 = set(i.strip() for i in f.read().split("\n"))

with open("../data/t50.txt") as f:
    t50 = set(i.strip() for i in f.read().split("\n"))

t25_count = sum(colleges[i] for i in t25)
t50_count = sum(colleges[i] for i in t50)

total = sum(colleges.values())

print(f"People in T20(25): {t25_count}, % of commitments: {t25_count / total * 100 : .2f}%")
print(f"People in T50: {t50_count}, % of commitments: {t50_count / total * 100 : .2f}%")
