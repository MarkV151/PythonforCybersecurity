#!/usr/bin/env python3
# example workign with Functions
def send_message():
    userInput = input("Is today a good day? (y/n) ")
    if userInput == "y":
        for i in range(10):
            print("Yes it is")
    else:
        print("No its not")
send_message()