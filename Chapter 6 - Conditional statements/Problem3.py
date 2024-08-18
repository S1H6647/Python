# A spam comment is defined as a test containing following keywords:
# "Make a lot of money", "buy now", "subscribe this", "click this". 
# Write a program to detect these spams.

def check_spam_comment(word):
    if ("make a lot of money" in word) or ("buy now" in word) or ("subscribe this" in word) or ("click this" in word):
        print("Spam comment detected!")
    else:
        print("Okay comment!")

string = input("Enter anything: ")
word = string.lower()
check_spam_comment(word)


