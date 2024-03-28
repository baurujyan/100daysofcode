import math

NAME = "the tip calculator"

print(f"Welcome to {NAME}!")
total_bill = float(input(f"What was the total bill: $"))
tip_amount = int(input(f"How much tip would you like to give? 10, 12, or 15? "))
ppl_amount = int(input(f"How many peope to split the bill? "))
price_per_person = (total_bill + total_bill * tip_amount / 100) / ppl_amount
print(f"Each person should pay: ${format(price_per_person, ".2f")}")