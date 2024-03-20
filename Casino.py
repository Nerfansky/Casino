import random
import math
import time


from statistics import mean
def get_Bet():
    while True:
        Bet = input("Make A Bet:")
        if Bet.isdigit():
            return int(Bet)
        else:
            print("Your Bet:   ", Bet, "is incorrect")

def game_logic():
    Symbols = ["apple", "pear", "cherry", "orange", "jackpot", "zero"]
    Coefficient = {
        "apple": 1,
        "pear": 1.5,
        "zero": 0.1,
        "cherry": 5,
        "orange": 0.5,
        "jackpot": 10
    }

    chances = {
        "apple": 20,
        "pear": 10,
        "zero": 30,
        "cherry": 5,
        "orange": 35,
        "jackpot": 0.00000000000001
    }

    def spin(chances):
        result = []
        for _ in range(1):
            symbols = random.choices(Symbols, weights=list(chances.values()), k=3)
            result.append(symbols)
        return result[0]

    while True:
        bet = get_Bet()
        if bet:
            spin_result = spin(chances)
            print("Spinning The Wheel\n")
            time.sleep(3)

            for _ in range(3):
                print("rolling\n")
                time.sleep(1)
            print("Spin Result:\n\n", spin_result,"\n")
            break

    convertations = [Coefficient[word] for word in spin_result]
    avg = mean(convertations)
    average = (round(avg))
    Balance = average * bet
    print("your winnings are", Balance , "$")


game_logic()

