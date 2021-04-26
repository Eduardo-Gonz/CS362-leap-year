# Directions to run this file:
# 1. Open terminal
# 2. Navigate to directory that this file is in
# 3. Run this command in terminal: "python Eduardo_Gonzalez_hw1.py"

def is_leap_year():
    year = int(input("Enter a leap year: "))

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

is_leap_year()