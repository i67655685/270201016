number_1 = input("Please enter the first number: ")
number_2 = input("Please enter the second number: ")
number_3 = input("Please enter the third number: ")

if number_1 < number_2 and number_1 < number_3:
  print("Minimum number is, ", number_1)
elif number_2 < number_1 and number_2 < number_3:
  print("Minimum number is, ", number_2)
elif number_3 < number_1 and number_3 < number_2:
  print("Minimum number is, ", number_3)