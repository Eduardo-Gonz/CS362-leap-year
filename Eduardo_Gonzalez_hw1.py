# Directions to run this file:
# 1. Open terminal
# 2. Navigate to directory that this file is in
# 3. Run this command in terminal: "python Eduardo_Gonzalez_hw1.py"


def validate_input():
    while True:
        try:
            yearInput = int(input("Enter a year: "))
        except ValueError:
            print("That is not an integer! Please try again")
            continue
        else:
            #validateRange(yearInput)
            break

    is_leap_year(yearInput)

def is_leap_year(year):

    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                print("{0} is a leap year !".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year !".format(year))
    else:
        print("{0} is not a leap year".format(year))

validate_input()



