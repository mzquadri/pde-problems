"""A small command-line Snake, Water, Gun game."""

from __future__ import annotations

import random

CHOICES = ("s", "w", "g")
NAMES = {"s": "Snake", "w": "Water", "g": "Gun"}


def game_win(computer: str, player: str) -> bool | None:
    """Return True for a player win, False for a loss, and None for a tie."""
    if computer not in CHOICES or player not in CHOICES:
        raise ValueError("Choices must be 's', 'w', or 'g'.")
    if computer == player:
        return None
    return (computer, player) in {("s", "g"), ("w", "s"), ("g", "w")}


def prompt_choice() -> str:
    while True:
        choice = input("Your turn [s]nake, [w]ater, or [g]un: ").strip().lower()
        if choice in CHOICES:
            return choice
        print("Please enter s, w, or g.")


def main() -> None:
    computer = random.choice(CHOICES)
    player = prompt_choice()
    result = game_win(computer, player)

    print(f"Computer chose {NAMES[computer]}.")
    print(f"You chose {NAMES[player]}.")
    if result is None:
        print("The game is a tie!")
    elif result:
        print("You win!")
    else:
        print("You lose!")


if __name__ == "__main__":
    main()
