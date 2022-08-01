import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

person_who_will_pay = random.choice(names)

print(person_who_will_pay + " is going to buy the meal today!")
