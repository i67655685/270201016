numbers = int(input("How many numbers: "))
for i in range(numbers):
  number = int(input("Enter the number: "))
  if (number % 2) == 0:
    print("{0} is Even".format(number))
  else:
    print("{0} is Odd".format(number))

# I can not solve for % of evens 
