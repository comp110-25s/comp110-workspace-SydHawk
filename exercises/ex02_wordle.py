"""Wordle Assignment"""

__author__: str = "730663953"


def contains_char(code_word: str, single_character: str) -> bool:
    """referencing given character to secret word"""
    assert len(single_character) == 1, f"len('{single_character}') is not 1"
    i: int = 0
    while i < len(code_word):
        if single_character == code_word[i]:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """testing for yellow or white box codification"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    result: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1
    return result


def input_guess(expected_length: int) -> str:
    """comparing user guess to expected code word length"""
    guess = input(f"Enter a {expected_length} char word:")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again:")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1
    max_turn = 6
    won = False
    while turn <= max_turn and not won:
        print(f"=== Turn {turn}/{max_turn} ===")
        guess = input_guess(len(secret))
        emoji_result = emojified(guess, secret)
        print(emoji_result)
        if guess == secret:
            won = True
            print(f"You won in {turn}/{max_turn} turns!")
            return
        turn += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
