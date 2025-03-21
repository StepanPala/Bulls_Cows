"""This module contains the helper functions for the Bulls & Cows game."""
import random

DASH_SEPARATOR = '-' * 47

def generate_number(num_digits=4) -> str:
    """Generates a random four-digit number with unique digits
    and not beginning with "0".
    
    Args: num_digits (int): Number of digits, default is 4.
    
    Returns:
        str: Generated number to be guessed.
    """
    while True:
        numbers = list(range(10))
        random.shuffle(numbers)
        gen_number = "".join(map(str, numbers[:num_digits]))

        if gen_number[0] != '0':
            return gen_number

def players_guess(num_digits: int) -> str:
    """Gets input from the player.
    
    Args: num_digits (int): Number of digits to be guessed.
    
    Returns:
        str: Player's guess.

    Raises:
        ValueError: If the guess is invalid.
    """
    while True:
        guess = input(
            f"{DASH_SEPARATOR}\n"
            ">>> "
            )

        if (
            len(guess) == num_digits
            and guess.isdigit()
            and guess[0] != '0'
            and len(set(guess)) == num_digits
        ):
            return guess

        print(
            "The number must have four digits, must not begin\n"
             "with \"0\" and each digit must be unique."
            )

def calculate_guesses(gen_number, guess) -> tuple[int, int]:
    """Calculates the number of bulls and cows.
    
    Args:
        gen_number (str): The number to be guessed.
        guess (str): Player's guess.
        
    Returns:
        tuple: Contains the number of bulls and cows.
    """
    bulls = 0
    cows = 0

    for i, digit in enumerate(guess):
        if digit == gen_number[i]:
            bulls += 1
        elif digit in gen_number:
            cows += 1

    return bulls, cows

def results(bulls, cows):
    """Prints the results.
    
    Args:
        bulls (int): Number of bulls.
        cows (int): Number of cows.
    """
    bull_num = "bull" if bulls == 1 else "bulls"
    cow_num = "cow" if cows == 1 else "cows"

    print(f"{bulls} {bull_num}, {cows} {cow_num}")

def play_game(num_digits=4):
    """The main game function.
    
    Args:
        num_digits (int): Number of digits, default is 4.
    
    Returns:
        None
    """
    gen_number = generate_number(num_digits)
    guesses = 0

    while True:
        guess = players_guess(num_digits)
        guesses += 1

        bulls, cows = calculate_guesses(gen_number, guess)
        results(bulls, cows)

        if bulls == num_digits:
            print(
                "Correct, you've guessed the right number\n"
                f"in {guesses} guesses!\n"
                f"{DASH_SEPARATOR}\n"
                "That's amazing!"
            )
            break
