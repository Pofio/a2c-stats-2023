import csv
import re
from datetime import datetime
import os

# YY, MM, DD
oldest = datetime(2022, 11, 1)

messages = []

with open("a2c_results.csv", encoding="iso-8859-1") as f:
    reader = csv.reader(f)
    for i in reader:
        try:
            dt = datetime.strptime(i[2], "%m/%d/%Y %I:%M %p")
        except ValueError:
            continue

        if dt > oldest:
            messages.append((i[1], re.sub(r'[^\x00-\x7F]+', '', i[3])))

os.makedirs("fragments", exist_ok=True)

PROMPT = 'I will give you a series of messages that are separated by a <br> tag. For each message, I will tell you the discord user who wrote the message and I want you to identify the university the person is going to and the major they want to do. If you cannot identify the major, use UNKNOWN. For each message, I want you to respond in the format of "author - university name - major"'
USERS_PER_FRAGMENT = 30

for i in range(0, len(messages), USERS_PER_FRAGMENT):
    with open(f"fragments/fragment{i // USERS_PER_FRAGMENT}.txt", "w", encoding="iso-8859-1") as f:
        f.write(PROMPT + "\n\n" + "\n<br>\n".join(f"{j[0]} wrote \"{j[1]}\"" for j in messages[i:i + USERS_PER_FRAGMENT]))
