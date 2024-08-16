# Write a program to create a dictionary of Nepali words with values as their English translation. 
# Provide user with an option to look it up!

nepaliWords = {
    "baba": "Father",
    "ama": "Mother",
    "didi": "elder sister",
    "bhai": "Younger brother",
    "Baini": "Younger sister"
}

enteredWords = input("Enter the  word you want meaning of: ")

meaningWords = nepaliWords[enteredWords]
# if the eneteredWords is in the dictionary nepaliWords then it returns the value of the entered word

print("The meaning to the word you enetered is:",meaningWords)

