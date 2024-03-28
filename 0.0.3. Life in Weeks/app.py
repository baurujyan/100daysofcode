MAXLIFE = 4000

age = int(input("Enter your age: "))

lived_weeks = int((age / 90) * MAXLIFE)


print(f"You lived {lived_weeks:,} weeks, left {(MAXLIFE - lived_weeks):,} weeks.")