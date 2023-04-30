# A2C Commitment Statistics

Using ChatGPT to extract uni/majors & Python to parse & load data

Prompt: `I will give you a series of messages that are separated by a <br> tag. 
For each message, I will tell you the discord user who wrote the message and I want you to identify the university 
the person is going to and the major they want to do. If you cannot identify the major, 
use UNKNOWN. For each message, I want you to respond in the format of "AUTHOR - UNIVERSITY NAME - MAJOR."`

Steps:

CSV exported through Discord Chat Exporter

Run `preprocessing.py` to generate the fragments

Paste whatever in each fragment into ChatGPT

Paste result into `result.txt`

Run `postprocessing.py` (just converts to json)

Do final touchups