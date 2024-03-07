import random

symbols = ["apple", "pear", "cherry", "orange", "jackpot", "zero"]
#chances for fruits
chances = {
    "apple": 0.2,    # x1
    "pear": 0.1,     # x1.5
    "zero": 0.3,     # x0
    "cherry": 0.1,   # x5
    "orange": 0.2,   # x0.5 coefficient
    "jackpot": 0.1   # won all
}

def spin():
    """Rolling game machine"""
    result = []
    for _ in range(3):
        symbol = random.choices(symbols, weights=list(chances.values()))[0]
        result.append(symbol)
    return result

def calculate_payout(spin_result, bet):
    """Calculation of winnings or losses"""
#Personally game logic
#comeback result

def play_game():
    """Button to start the game"""
    bet = 0  # Players wager
    # second logic up betts, rolling, calculate gaings,

if __name__ == "__main__":
    # just dummy line
    play_game()
