print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill=5
    print("Child ticket is $5")
  elif age <= 18:
    bill=7
    print("Youth ticket is $7")
  else:
    bill=12
    print("Adult ticket is $12")

  print("if you want a photo you have to pay additional $3.")
  want_photo=input("Do you want a photo taken? (Y or N) ")
  if want_photo=="Y":
    bill+=3
    print(f"Your final bill is ${bill}")
  else:
    print(f"Your final bill is ${bill}")
    
else:
  print("Sorry, you have to grow taller before you can ride.")
