year = ""
tried_years = []
correct = False

def leap_year_checker(input_year):
    if input_year % 4 == 0:
        if input_year % 100 == 0:
            if input_year % 400 == 0:
                print(f"The {input_year} year is a leap year.")
            else:
                print(f"The {input_year} year is NOT a leap year.")
        else:
            print(f"The {input_year} year is a leap year.")
    else:
        print(f"The {input_year} year is NOT a leap year.")
    tried_years.append(input_year)

def user_input():
    global correct
    user_inputted_year = input("Input a year: ")
    if user_inputted_year.lower() == "stop":
        pass
    else:    
        try:
            user_inputted_year = int(user_inputted_year)
            correct = True
            return user_inputted_year
        except:
            print("Please, input a number as a year.")

user_input()

while year.lower() != "stop":
    correct = False
    while correct == False:
        year = user_input()
        if year in tried_years:
            print(f"The {year} year has already been checked. Try again another year.")
        else:
            leap_year_checker(year)
            print("Type \"stop\" to finish.")