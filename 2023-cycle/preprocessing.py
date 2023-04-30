import csv
import re
from datetime import datetime
import os

# YY, MM, DD
oldest = datetime(2022, 11, 1)

messages = []

with open("../a2c_results.csv", encoding="iso-8859-1") as f:
    reader = csv.reader(f)
    for i in reader:
        try:
            dt = datetime.strptime(i[2], "%m/%d/%Y %I:%M %p")
        except ValueError:
            continue

        if dt > oldest:
            messages.append((i[1], re.sub(r'[^\x00-\x7F]+', '', i[3]).replace("\n", "")))

os.makedirs("fragments", exist_ok=True)

PROMPT = 'I will give you a series of messages written by different discord users which are separated by a new line. For each message, the author has said which university they are going to and potential areas they are interested in doing. I want you to identify the university name and the potential areas they are interested in doing. If you cannot identify the major, use UNKNOWN. If you cannot identify the university, use UNKNOWN. I want you to use university names recognized by usnews. Respond in a format like this: "author - university name - area1, etc" where the interested areas is a comma separated list. I want you to make the interested areas be standardized and have their full names without any extra modifiers. Do not add any extra "and\'s" in the response, separate interested areas using a comma, separate majors and minors, ignore concentrations, do not use forward slashes, ignore honors college, ignore schools/colleges within the university.'
USERS_PER_FRAGMENT = 25

for i in range(0, len(messages), USERS_PER_FRAGMENT):
    with open(f"fragments/fragment{i // USERS_PER_FRAGMENT}.txt", "w", encoding="iso-8859-1") as f:
        f.write(PROMPT + "\n\n" + "\n".join(f"{j[0]} wrote \"{j[1]}\"" for j in messages[i:i + USERS_PER_FRAGMENT]))
