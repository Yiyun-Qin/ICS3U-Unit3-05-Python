#!/usr/bin/env python3

# Created by Yiyun Qin
# Created on March 2022
# This is the math program, showing the month according to the number


def main():
    # This function shows the actual month

    # input
    number_month = int(input("Enter the month number as a number between 1-12: "))

    # process & output
    print("")
    if number_month == 1:
        print("It is January.")
    elif number_month == 2:
        print("It is February.")
    elif number_month == 3:
        print("It is March.")
    elif number_month == 4:
        print("It is April.")
    elif number_month == 5:
        print("It is May.")
    elif number_month == 6:
        print("It is June.")
    elif number_month == 7:
        print("It is July.")
    elif number_month == 8:
        print("It is August.")
    elif number_month == 9:
        print("It is September.")
    elif number_month == 10:
        print("It is October.")
    elif number_month == 11:
        print("It is November.")
    elif number_month == 12:
        print("It is December.")
    else:
        print("This is not a number of month!")
    print("\nDone.")


if __name__ == "__main__":
    main()
