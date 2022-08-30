"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730489241"

input_word: str = input("Enter a 5-character word: ")
if len(input_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character")
    exit()
print("Searching for " + single_character + " in " + input_word)

instances: int = 0

if input_word[0] == single_character:
    print(single_character + " found at index 0")
    instances = instances + 1

if input_word[1] == single_character:
    print(single_character + " found at index 1")
    instances = instances + 1

if input_word[2] == single_character:
    print(single_character + " found at index 2")
    instances = instances + 1

if input_word[3] == single_character:
    print(single_character + " found at index 3")
    instances = instances + 1

if input_word[4] == single_character:
    print(single_character + " found at index 4")
    instances = instances + 1

if instances == 0:
    print("No instances of " + single_character + " found in " + input_word)

if instances == 1:
    print(str(instances) + " instance of " + single_character + " found in " + input_word)

if instances >= 2:
    print(str(instances) + " instances of " + single_character + " found in " + input_word)