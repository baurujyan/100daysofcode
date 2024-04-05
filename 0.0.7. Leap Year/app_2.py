print(f"Welcome to the Leap year checker program. (Please, type \"stop\" to finish checking.)")
checked_years = []

def start():
    current_input = user_input()
    if current_input.lower() == "stop":
        print("Program has been shut down.")
        return 0
    else:
        try:
            current_input = int(current_input)
            if current_input in checked_years:
                print(f"The year {current_input} has already been checked. Please, input another year.")
                start()
            else:
                leap_check(current_input)
                checked_years.append(current_input)
                start()
        except:
            print("Please, print a year in numbers.")
            start()

def user_input():
    input_by_user = input("Input a year: ")
    return input_by_user

def leap_false(year):
    print(f"The year {year} is NOT a leap year.")
    return 0

def leap_true(year):
    print(f"The year {year} is a leap year.")
    return 0

def leap_check(year):
    if year % 4 != 0:
        leap_false(year)
    else:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_true(year)
            else:
                leap_false(year)
        else:
            leap_true(year)

start()