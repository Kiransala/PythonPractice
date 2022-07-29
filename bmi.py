height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

w = int(weight)
h = float(height)

bmi = w / (h * h)

bmi_as_int = int(bmi)
print(bmi_as_int)