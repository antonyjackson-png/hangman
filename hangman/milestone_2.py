import random

word_list = ["Apple", "Banana", "Grapes", "Orange", "Lemon"]
print(word_list)

word = random.choice(word_list)
print(word)

alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

guess = input("Enter a single letter: ")

if len(guess) == 1 and guess.lower() in alphabet:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")


