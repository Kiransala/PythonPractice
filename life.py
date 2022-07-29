age = input("What is your current age?")

a=int(age)
years_remain=(90-a)
ydays=(years_remain*365)
yweeks=(years_remain*52)
ymonths=(years_remain*12)

print(f"You have {ydays} days, {yweeks} weeks, and {ymonths} months left.")
