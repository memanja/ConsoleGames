import random

import pyfiglet
from tabulate import tabulate


def start_game1():
    play = True
    digits = list(range(10))
    random.shuffle(digits)
    target = "".join(map(str, digits[:4]))
    while play:
        correct_place = 0
        correct_number = 0
        my_guess = input('Guess ').strip()

        if my_guess == target:
            print(pyfiglet.figlet_format("CONGRATZZ!!\n" + target))
            break

        used_chars = [False] * len(target)
        for i in range(len(my_guess)):
            if i < len(target) and my_guess[i] == target[i]:
                correct_place += 1
                used_chars[i] = True
        for i in range(len(my_guess)):
            if i < len(target) and my_guess[i] != target[i] and my_guess[i] in target:
                for j in range(len(target)):
                    if not used_chars[j] and my_guess[i] == target[j]:
                        correct_number += 1
                        used_chars[j] = True
                        break

        headers = ["Correct Place and number", "Correct Number but not place"]
        values = [[correct_place, correct_number]]
        print(tabulate(values, headers, tablefmt="plain"))


start_game1()
