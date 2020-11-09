a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))

power_of_a = 1

for i in range(b):
  power_of_a *= a
print(power_of_a)