"""EX06 - Choose Your Own Adventure - Flip a Coin."""

__author__ = "730489241"

from random import randint

player: str = ""
points: int = 10
playing: bool = True
RAND_FLIP_START: int = 0
RAND_FLIP_END: int = 10
END_LIMIT: int = 500
MONEY: str = "\U0001F4B2"


def greet() -> None:
    """Greets the player."""
    global points
    global player 
    player = input("Please enter your name: ")
    print(f"Hello {player}! Thank you for playing!")
    print("\n")
    print(f"This game is called 'Heads or Tails'! You start off with a balance of {MONEY}{points}")
    print("and you are to place a bet on whether a coin, when flipped, will land on heads or tails!")
    print("If you guess correctly, your bet is doubled!")
    print("If not, your bet will be lost!")
    print("\n")
    

def flip() -> str:
    """Flips the coin."""
    flip: int = randint(RAND_FLIP_START, RAND_FLIP_END)
    result: str = ""
    if flip == 0:
        result = str("Sorry! The coin fell off the table! You lost...")
    if flip % 2 == 0:
        result = str("Heads")
    else:
        result = str("Tails")
    return result
    

def check_guess(guess: str, results: str) -> bool:
    """Checks the guess against the result of the flip."""
    if guess == "Head" or guess == "head":
        guess = "Heads"
    if guess == "Tail" or guess == "tail":
        guess = "Tails"
    if guess == results:
        print(f"Congrats! You guessed that the coin would land on {results} correctly! Your balance is increased!")
        return True
    if results == "Heads" or results == "Tails":
        print(f"Sorry, the coin flipped {results}. You lost...")
        return False
    print(results)
    return False


def do_guess() -> str:
    """Asks for guess."""
    guess: str = input("What is your guess? Please type 'Head' or 'Tail'! You can also type 'Quit' to quit!: ")
    while guess != "Head" and guess != "Tail" and guess != "head" and guess != "tail":
        if guess == str("Quit") or guess == str("quit"):
            quit()
        guess = input("Sorry! That input was invalid! Please try again!: ")
    return guess


def win(bet: int, points: int) -> int:
    """Doubles points on a win."""
    return (bet * 2) + (points - bet)
    

def loss(bet: int, points: int) -> int:
    """Subtracts bet from points."""
    return points - bet


def main() -> None:
    """Conducts main functions."""
    greet()
    global playing
    global points
    while playing:   
        print(f"Your current balance is {MONEY}{points}!")
        bet: int = int(input("Please enter a NUMERICAL bet: "))
        while bet < 0 or bet == 0 or bet > points:
            bet = int(input("Invalid bet placement, try again: "))
        if check_guess((do_guess()), (flip())):
            points = win(bet, points)
        else:
            points = loss(bet, points)
        if points > END_LIMIT:
            print("Congrats! You stole all of our money! Come again later!")
            playing = False
        if points <= 0:
            print("Sorry! You're out of money! Try again later!")
            playing = False


if __name__ == "__main__":
    main()