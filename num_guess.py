#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sep 2019
# This program checks if there is over 30 students


import random
import sys


def main():
    # this function checks if there is over 30 students

    # input
    biggest_num = int(input("Enter the largest number to be generated: "))
    users_num = int(input("Guess a number between 1 and {:}: ".format(biggest_num)))
    random_num = random.randint(1, biggest_num)
    if users_num == random_num:
        print("Good job you won!")
    else:
        print("Sorry wrong number.:( The correct number was {}".format(random_num))

    try_again = str(input("Would you like to try again? \n"))
    if try_again == "Y" or try_again == "y" or try_again == "yes" or try_again == "YES":
        main()
    elif try_again == "N" or try_again == "n" or try_again == "no" or try_again == "NO":
        sys.exit()


if __name__ == "__main__":
    main()
