"""
Main module for the Bulls & Cows game.
It contains the game introduction and starts the game.
"""
from helper import play_game, DASH_SEPARATOR

# Game introduction
print(f"""
Hi there!
{DASH_SEPARATOR}
I've generated a random 4-digit number for you.
Let's play a bulls and cows game.
{DASH_SEPARATOR}
Enter a number: """)

if __name__ == "__main__":
    play_game()
