programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again."
}

#Retreving item from dictionary
print(programming_dictionary["Bug"])

#Adding an item to dictionary
programming_dictionary["Loop"]="The action of doing some thing again and again."
print(programming_dictionary)

#Create an empty dictionary
empty_dictionary={}
print(empty_dictionary)

#Edit an item in dictionary
programming_dictionary["Bug"]="A moth in your computer."

#Loop in dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])