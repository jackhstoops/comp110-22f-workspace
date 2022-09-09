"""EX02 - Wordle - One Shot Wordle"""

__author__ = "730489241"


secret: str = "python"
input_word: str = input("What is your 6-letter guess? ")
while len(input_word) != 6:
    input_word = input("That was not 6 letters! Try again: ")

i = 0
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
white_box: str = "\U00002B1C"
final: str = ""
p: bool = False
is_winner: bool = True

while i < 6:
    if input_word[i] == secret[i]:
        final = final + green_box  
    elif input_word[i] in secret:
        final = final + yellow_box
        is_winner = False
    else:
        final = final + white_box
        is_winner = False
    i += 1

print(final)
if is_winner:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
