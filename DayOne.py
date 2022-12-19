"""
Advent of Code Day 1
Puzzle 1: Calorie counting:
    Find the Elf carrying the most Calories. How many total Calories is
    that Elf carrying?
Puzzle 2:
    Find the top three Elves carrying the most Calories. How many Calories are
    those Elves carrying in total?
All code written by Leon Nitsch
"""
from typing import Union


def calorie_counter(elves: list[Union[list[int], int]]) -> list:
    """
    Given a list of elves and how many calories per ration that they have, return a list of the total calories of each elf
    :param elves: list of calories of items that they have
    :return: list of total calories per elf
    """
    for pos in range(len(elves)):
        elves[pos] = sum(elves[pos])

    return elves


if __name__ == "__main__":
    mode = input("Press 1 for Puzzle 1 solver, press 2 for Puzzle 2 solver:\n")
    if mode == "1":
        total_elves = []
        elf = []
        with open(input("File of elves and calorie count:")) as file:
            for line in file:
                if not line.isspace():
                    elf.append(int(line))
                else:
                    total_elves.append(elf)
                    elf = []

        print("The max number of calories a single elf holds is: {}".format(max(calorie_counter(total_elves))))

    elif mode == "2":
        total_elves = []
        elf = []
        with open(input("File of elves and calorie count:")) as file:
            for line in file:
                if not line.isspace():
                    elf.append(int(line))
                else:
                    total_elves.append(elf)
                    elf = []
        condensed_elves = calorie_counter(total_elves)
        total = max(condensed_elves)
        print("The max number of calories a single elf holds is: {}".format(max(condensed_elves)))

        condensed_elves.remove(max(condensed_elves))
        total += max(condensed_elves)
        print("The second most number of calories a single elf holds is: {}".format(max(condensed_elves)))

        condensed_elves.remove(max(condensed_elves))
        total += max(condensed_elves)
        print("The third most number of calories a single elf holds is: {}".format(max(condensed_elves)))

        print("Their total calories are: {}".format(total))
    else:
        print("Please choose a valid input")
