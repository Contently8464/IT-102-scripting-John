#!/usr/bin/env python3
# example workign with Loops
#By 
vibe = input('Is today a good day? (y/n) ')
if vibe == 'y':
    number = 1
    while number < 11:
        print ("I'm glad you're having a good day")
        number += 1
elif vibe == "n":
    print ("I'm sorry to hear that.")
else:
    print ("Please input y or n")