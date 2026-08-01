import unittest

from main import game_win


class GameWinTests(unittest.TestCase):
    def test_ties(self) -> None:
        for choice in ("s", "w", "g"):
            self.assertIsNone(game_win(choice, choice))

    def test_each_winning_matchup(self) -> None:
        self.assertTrue(game_win("s", "g"))
        self.assertTrue(game_win("w", "s"))
        self.assertTrue(game_win("g", "w"))

    def test_invalid_choice(self) -> None:
        with self.assertRaises(ValueError):
            game_win("s", "x")


if __name__ == "__main__":
    unittest.main()
