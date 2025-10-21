#!/usr/bin/env python3
# Sample script that writes to a file
# By John  
questions = [
    "What is your name? ",
    "What is your favorite color? ",
    "What was your first pet's name? ",
    "What is yourmother's maiden name? ",
    "What elementary school did you attend? ",

]

answers = []
for q in questions:
    ans = input(q)
    answers.append(ans)

with open("hackme.txt", "w") as file:
    for line in answers:
        file.write(line + "\n")

with open("hackme.txt", "r") as example:
    content = example.read()
    print(content)