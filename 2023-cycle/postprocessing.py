import re
import json

with open("result/result.txt", encoding="iso-8859-1") as f:
    data = [[j.strip() for j in i.split(" - ")] for i in re.split("\n+", f.read())]

for i in data:
    i[2] = [j.strip() for j in i[2].split(", ")]

# OLD CODE
# with open("result/result.txt", encoding="iso-8859-1") as f:
#     data = [[j.strip() for j in i.split(" - ", 2)] for i in re.sub(r"\s*<br>\s*", "\n", f.read()).split("\n")]
#
# for i in data:
#     i[2] = [i[2].lower()]

with open("result/result.json", "w", encoding="iso-8859-1") as f:
    json.dump(data, f, indent=2)
