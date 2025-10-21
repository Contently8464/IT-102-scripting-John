vibe = input('Is today a good day? (y/n) ')
def send_message():
    if vibe == '':
        print ("Please input y or n")
    elif vibe == "y":
        print ("I'm glad you're having a good day")
    else:
        print ("I'm sorry to hear that.")

send_message()