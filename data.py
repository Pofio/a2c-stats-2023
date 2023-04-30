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

a = sorted(colleges.items(), key=lambda x: x[1], reverse=True)
b = sorted(interested_subjects.items(), key=lambda x: x[1], reverse=True)

for i in a:
    print(i)