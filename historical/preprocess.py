import csv
import re
from datetime import datetime
import os

years = {"2023": (datetime(2022, 11, 1), []), "2022": (datetime(2021, 11, 1), []), "2021": (datetime(2020, 11, 1), [])}

with open("../a2c_results.csv", encoding="iso-8859-1") as f:
    reader = csv.reader(f)
    for i in reader:
        try:
            dt = datetime.strptime(i[2], "%m/%d/%Y %I:%M %p")
        except ValueError:
            continue

        for j in years.values():
            if dt > j[0]:
                j[1].append((i[1], re.sub(r'[^\x00-\x7F]+', '', i[3]).replace("\n", "")))
                break

PROMPT = 'I will give you a series of messages written by different discord users which are separated by a new line. For each message, the author has said which university they are going to. I want you to identify the university name. If you cannot identify the university, use UNKNOWN. I want you to use university names recognized by usnews. Respond in a format like this: "author - university name" where the interested areas is a comma separated list. Ignore honors college, ignore schools/colleges within the university. Ignore potential majors they are interested in.'
USERS_PER_FRAGMENT = 40

for i, j in years.items():
    os.makedirs(f"years/{i}/fragments", exist_ok=True)
    for k in range(0, len(j[1]), USERS_PER_FRAGMENT):
        with open(f"years/{i}/fragments/fragment{k // USERS_PER_FRAGMENT}.txt", "w", encoding="iso-8859-1") as f:
            f.write(PROMPT + "\n\n" + "\n".join(f"{m[0]} wrote \"{m[1]}\"" for m in j[1][k:k + USERS_PER_FRAGMENT]))
