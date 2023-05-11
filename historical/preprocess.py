import csv
import re
from datetime import datetime
import os

import json

years = {"2023": (datetime(2022, 11, 1), []), "2022": (datetime(2021, 11, 1), []), "2021": ([])}

# with open("../a2c_results.csv", encoding="iso-8859-1") as f:
#     reader = csv.reader(f)
#     for i in reader:
#         try:
#             dt = datetime.strptime(i[2], "%m/%d/%Y %I:%M %p")
#         except ValueError:
#             continue
#
#         for j in years.values():
#             if dt > j[0]:
#                 j[1].append((i[1], re.sub(r'[^\x00-\x7F]+', '', i[3]).replace("\n", "")))
#                 break

persons_leaving = ([datetime(2022, 11, 1), 0], [datetime(2021, 11, 1), 0], [datetime(2020, 11, 1), 0])

with open("../a2c_results.json", encoding="iso-8859-1") as f:
    data = json.load(f)


def parse_prefix(line, fmt):
    try:
        t = datetime.strptime(line, fmt)
    except ValueError as v:
        if len(v.args) > 0 and v.args[0].startswith('unconverted data remains: '):
            line = line[:-(len(v.args[0]) - 26)]
            t = datetime.strptime(line, fmt)
        else:
            raise
    return t


for m in data["messages"]:
    dt = parse_prefix(m["timestamp"], "%Y-%m-%dT%H:%M:%S")

    for j in persons_leaving:
        if dt > j[0]:
            j[1] += not m["author"]["color"]
            break

print(persons_leaving)


# PROMPT = 'I will give you a series of messages written by different discord users which are separated by a new line. For each message, the author has said which university they are going to. I want you to identify the university name. If you cannot identify the university, use UNKNOWN. I want you to use university names recognized by usnews. Respond in a format like this: "author - university name" where the interested areas is a comma separated list. Ignore honors college, ignore schools/colleges within the university. Ignore potential majors they are interested in.'
# USERS_PER_FRAGMENT = 40
#
# for i, j in years.items():
#     os.makedirs(f"years/{i}/fragments", exist_ok=True)
#     for k in range(0, len(j[1]), USERS_PER_FRAGMENT):
#         with open(f"years/{i}/fragments/fragment{k // USERS_PER_FRAGMENT}.txt", "w", encoding="iso-8859-1") as f:
#             f.write(PROMPT + "\n\n" + "\n".join(f"{m[0]} wrote \"{m[1]}\"" for m in j[1][k:k + USERS_PER_FRAGMENT]))
