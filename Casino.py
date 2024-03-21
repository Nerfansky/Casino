import random
import math
import time
import os
from statistics import mean


def get_Bet(balance):
    while True:
        try:
            bet = int(input("Make A Bet (Your Balance is {}): ".format(balance)))
            if bet > 0 and bet <= balance:
                return bet
            else:
                print("make a correct bet!\n your max bet can be {}.".format(balance))
        except ValueError:
            print("enter a valid number")


def create_missing_files():
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
            "apple": 0.2,
            "pear": 0.1,
            "zero": 0.3,
            "cherry": 0.1,
            "orange": 0.2,
            "jackpot": 0.1
        }

        def spin(chances):
            result = []
            for _ in range(3):
                symbols = random.choices(Symbols, weights=list(chances.values()), k=3)
                result.append(symbols)
            return result[0]


        create_missing_files()

        try:
            with open("last_balance.txt", "r") as f:
                content = f.read()
                if content.strip():
                    balance = float(content)
                else:
                    while True:
                        initial_balance = input("how much dib you buy?  ")
                        if initial_balance.isdigit():
                            balance = float(initial_balance)
                            break
                        else:
                            print("enter a valid number.")
        except FileNotFoundError:
            while True:
                initial_balance = input("how much dib you buy?  ")
                if initial_balance.isdigit():
                    balance = float(initial_balance)
                    break
                else:
                    print("enter a valid number.")

        while True:
            bet = get_Bet(balance)
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
            win = average * bet
            balance += win
            print("Your winnings are", win, "$\n")
            print("Your current balance is", balance, "$\n")

            with open("last_balance.txt", "w") as f:
                f.write(str(balance))

            with open("Data_Base.txt", "a") as file:
                file.write(str(win) + "\n")

            if input("Continue playing (yes/no): ").lower() != "yes":
                clear_screen()
                break

    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except Exception as e:
        print("An error occurred:", e)
        with open("Fatal_error.txt", "a") as f:
            f.write("An error occurred: " + str(e) + "\n")

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    elif 'TERM' in os.environ:
        os.system('clear')

game_logic()
