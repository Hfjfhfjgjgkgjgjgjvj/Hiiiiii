import requests
import time

def kahoot_bot_spammer(pin: str, nickname: str, num_of_bots: int):
    """
    Function to spam a Kahoot game with multiple bots.

    Parameters:
    - pin: str
        The game PIN of the Kahoot game to join.
    - nickname: str
        The nickname to be used by the bots.
    - num_of_bots: int
        The number of bots to create and join the game.

    Raises:
    - ValueError:
        If the number of bots is less than or equal to zero.

    Returns:
    - int:
        The number of bots successfully joined the game.
    """

    # Checking if the number of bots is valid
    if num_of_bots <= 0:
        raise ValueError("Number of bots should be greater than zero.")

    # Counter to keep track of the number of bots joined
    bots_joined = 0

    # Loop to create and join the bots
    for i in range(num_of_bots):
        # Creating a unique nickname for each bot
        bot_nickname = f"{nickname}{i+1}"

        # Sending a POST request to join the game
        response = requests.post(f"https://kahoot.it/reserve/session/{pin}/", json={"nickname": bot_nickname})

        # Checking if the bot successfully joined the game
        if response.status_code == 200:
            bots_joined += 1

        # Delaying between each bot join request to avoid spamming the server
        time.sleep(0.5)

    return bots_joined

# Unit tests for kahoot_bot_spammer function.

import unittest

class TestKahootBotSpammer(unittest.TestCase):

    # Tests for valid inputs
    def test_kahoot_bot_spammer_with_valid_inputs(self):
        """
        Tests the function with valid inputs.
        """
        self.assertEqual(kahoot_bot_spammer("123456", "Bot", 5), 5)

    # Tests for invalid inputs
    def test_kahoot_bot_spammer_with_zero_bots(self):
        """
        Tests the function with zero bots. It should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            kahoot_bot_spammer("123456", "Bot", 0)

    def test_kahoot_bot_spammer_with_negative_bots(self):
        """
        Tests the function with negative number of bots. It should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            kahoot_bot_spammer("123456", "Bot", -5)

# Example usage of kahoot_bot_spammer function:

# Joining a Kahoot game with 10 bots
pin = "123456"
nickname = "Bot"
num_of_bots = 10
bots_joined = kahoot_bot_spammer(pin, nickname, num_of_bots)
print(f"Successfully joined {bots_joined} bots to the Kahoot game with PIN {pin}.")

# Joining a Kahoot game with zero bots (should raise an error)
try:
    bots_joined = kahoot_bot_spammer(pin, nickname, 0)
    print(f"Successfully joined {bots_joined} bots to the Kahoot game with PIN {pin}.")
except ValueError as e:
    print(f"Error while joining bots to the Kahoot game: {e}")
