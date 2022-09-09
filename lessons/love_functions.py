"""Love Functions ?"""

def love(subject: str) -> str:
    """Given a subject as a parameter, returns a loving string."""
    return f"I love you {subject}!!!!"

"""return != print"""

print(love("Jack"))


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n" #short for new line. what happens after you hit enter
        i += 1
    return love_note