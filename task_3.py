#!/usr/bin/env python3
import re


def main():
    def is_plate_valid(plate) -> bool:
        if not 2 <= len(plate) <= 6:
            return False
        if not re.search(r"^[A-Za-z]{2}[A-Za-z]*([1-9][0-9]*)?$", plate):
            return False
        return True
    plate_name = str(input("Please, input plate name: "))
    if is_plate_valid(plate_name):
        print("Valid plate!")
    else:
        print("Sorry, invalid plate")


if __name__ == "__main__":
    main()
