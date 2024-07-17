"""
The program allows for the user to enter a word and receive its definition
"""
from PyDictionary import PyDictionary

dictionary = PyDictionary()

print("Press enter without typing anything to exit.")
while True:
    word = input("Enter a word: ")
    if word == "":
        break
    else:
        print(dictionary.meaning(word))

