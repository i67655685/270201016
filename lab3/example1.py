asked_number = int(input("Please enter a number: "))

if asked_number >= 0:
  print("Absolute value of number is, ", asked_number)
elif asked_number < 0:
  asked_number_abs = int(asked_number)*(-1)
  print("Absolute value of number is, ", asked_number_abs)