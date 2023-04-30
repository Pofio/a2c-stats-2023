import json
import os

data = {}

for i in os.listdir("years"):
    with open(f"years/{i}/result/result.txt", encoding="iso-8859-1") as f:
        data[i] = [[j.strip() for j in i.split(" - ")][:2] for i in f.read().split("\n")]

with open("result/result.json", "w", encoding="iso-8859-1") as f:
    json.dump(data, f, indent=2)
