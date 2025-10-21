#!/usr/bin/env python3
# example workign with conditionals
#By John
vibe = input('Is today a good day? (y/n) ')
if vibe == '':
    print ("Please input y or n")
elif vibe == "y":
    print ("I'm glad you're having a good day")
else:
    print ("I'm sorry to hear that.")