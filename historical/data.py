import json
from collections import defaultdict

with open("result/result.json", encoding="iso-8859-1") as f:
    data = json.load(f)

colleges = defaultdict(lambda *x: 0)

for i in data.values():
    for j in i:
        colleges[j[1]] += 1

a = sorted(colleges.items(), key=lambda x: x[1], reverse=True)

for i in a:
    print(i)
