for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:  #if divisible by 3 and 5 print fizzbuzz
        print("FizzBuzz")
    elif number % 3 == 0:                    #if divisible by 3 print fizz
        print("Fizz")
    elif number % 5 == 0:                    #if divisible by 5 print buzz
        print("Buzz")
    else:
        print(number)                        #else print only numbers