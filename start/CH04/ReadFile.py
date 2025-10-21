#!/usr/bin/env python3
# Sample script that reads from a file
# By John
with open("hackme.txt", "r") as example:
    content = example.read()
    print("Here is someone to hack - information: ")
    print(content)