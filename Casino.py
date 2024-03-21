import random
import math
import time
import os
from statistics import mean


def get_Bet():
    while True:
        try:
            Bet = input("Make A Bet: ")
            if Bet.isdigit():
                if int(Bet) < 101:
                    return int(Bet)
                else:
                    print("Your Bet:", Bet, "is too high")
            else:
                print("Your Bet:", Bet, "is incorrect")
        except KeyboardInterrupt:
            raise KeyboardInterrupt


def create_missing_files():
    # Перевірка наявності файлів та їх створення, якщо вони відсутні
    for filename in ["last_balance.txt", "Balance.txt", "Data_Base.txt", "Fatal_error.txt"]:
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write("")


def game_logic():
    try:
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
            for _ in range(54):
                symbols = random.choices(Symbols, weights=list(chances.values()), k=3)
                result.append(symbols)
            return result[0]


        create_missing_files()


        try:
            with open("last_balance.txt", "r") as f:
                content = f.read()
                if content.strip():
                    last_balance = float(content)
                else:
                    last_balance = 0.0
        except FileNotFoundError:
            last_balance = 0.0

        bet = get_Bet()

        while True:
            spin_result = spin(chances)
            print("\nSpinning The Wheel\n")
            time.sleep(3)

            for _ in range(3):
                print("rolling\n")
                time.sleep(1)
            print("Spin Result:\n\n", spin_result, "\n")

            convertations = [Coefficient[word] for word in spin_result]
            avg = mean(convertations)
            average = (round(avg))
            balance = average * bet
            print("Your winnings are", balance, "$\n")


            with open("last_balance.txt", "w") as f:
                f.write(str(balance))

            with open("Data_Base.txt", "a") as file:
                file.write(str(balance) + "\n")

            if input("take bet and get away (yes/no): ").lower() != "no":
                if os.name == 'nt':
                    os.system('cls')
                elif 'TERM' in os.environ:
                    os.system('clear')
                break

            with open("Balance.txt", "w") as f:
                f.write(str(balance))
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except Exception as e:
        print("An error occurred:", e)
        print("Debug information:")
        print("Bet:", bet)
        print("Spin result:", spin_result)
        with open("Fatal_error.txt", "a") as f:
            f.write("An error occurred: " + str(e) + "\n")
            f.write("Debug information:\n")
            f.write("Bet: " + str(bet) + "\n")
            f.write("Spin result: " + str(spin_result) + "\n")


game_logic()
