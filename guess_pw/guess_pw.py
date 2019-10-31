# Input an 8-character password and find out how many guesses it takes for the program to find that password.

import random
import sys
sys.setExecutionLimit(360000) # 360 seconds
my_pw = input("Enter your 8-character password:")

def guess_pw(pw):
    guess_num = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    done = False
    while not done:
        guessed_pw = ""
        # your code here
        for _ in range(8):
            guessed_pw += alphabet[random.randrange(len(alphabet))]
        guess_num += 1
        if guessed_pw == pw:
            print("found it after", guess_num, "tries")
            done = True
    return guess_num

guess_pw(my_pw)