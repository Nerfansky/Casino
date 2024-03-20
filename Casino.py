import random
import math
import time

def get_Bet():
    while True:
        Bet = input("Make A Bet: ")
        if Bet.isdigit():
            return int(Bet)
        else:
            print("Your Bet:", Bet, "is incorrect")

def game_logic():
    Symbols = ["apple", "pear", "cherry", "orange", "jackpot", "zero"]
    apple, pear, zero, cherry, orange, jackpot = 1, 1.5, 0, 5, 0.5, 777
    apple_chance, pear_chance, zero_chance, cherry_chance, orange_chance, jackpot_chance = 0.2, 0.1, 0.3, 0.1, 0.2, 0.1
    Coefficient = {
        apple: 1,
        pear: 1.5,
        zero: 0,
        cherry: 5,
        orange: 0.5,
        jackpot: 777
    }

    chances = {
        "apple": 20,
        "pear": 10,
        "zero": 30,
        "cherry": 5,
        "orange": 35,
        "jackpot": 0.01
    }

    def spin(chances):
        result = []
        for _ in range(3):
            symbols = random.choices(Symbols, weights=list(chances.values()), k=3)
            result.append(symbols)
        return '\n'.join([str(x) for x in result])

    while True:
        bet = get_Bet()
        if bet:
            spin_result = spin(chances)

            for _ in range(3):
                print("rolling\n")
                time.sleep(1)

            print("Spin result:\n\n", spin_result)

            break  #тимчасово


game_logic()
