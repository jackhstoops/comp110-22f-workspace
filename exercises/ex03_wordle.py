"""EX03 - Wordle."""

__author__ = "730489241"

"""Define input_word as user's input """
def input_guess(word_len: int) -> str:

    user_guess: str = input(f"Enter a {word_len} characrter word: ")
    while len(user_guess) != word_len:
        user_guess = input(f"That wasn't {word_len} chars! Try again: ")   
    return user_guess

def contains_char(secret: str, input_char: str) -> bool:
    assert len(input_char) == 1
    i = 0
    while i < len(secret):
        if input_char == secret[i]:
            return True
        else:
            i += 1
    return False

def emojified(input_word: str, secret: str) -> str:
    assert len(input_word) == len(secret)    
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    white_box: str = "\U00002B1C"
    final: str = ""
    i = 0
    while i < len(secret):
        if input_word[i] == secret[i]:
            final = final + green_box  
        elif contains_char(secret, input_word[i]):
            final = final + yellow_box
        else:
            final = final + white_box
        i += 1
    return final

def main() -> None:
    turn: int = 1
    secret: str = "codes"
    secret_len: int = len(secret)
    yellow_box: str = "\U0001F7E8"
    white_box: str = "\U00002B1C"
    i = 0

    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        input_word: str = input_guess(secret_len)
        boxes: str = emojified(input_word, secret)
        print(emojified(input_word, secret))
        
        if not (contains_char(boxes, yellow_box) or contains_char(boxes, white_box)):
            print(f"You won in {turn}/6 turns!")
            exit()
        else:
          turn += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()