value_of_year = int(input("Please enter a year: "))

if value_of_year % 4:
  if value_of_year % 400 == 0:
    print(value_of_year, "is a leap year!")
  elif value_of_year % 400 != 0:   #There is some problem like that this line of code does not work with year 1900 and ı actually don't get ıt why.
    print(value_of_year, "is not a leap year!")
else :
  print(value_of_year, "is a leap year!")

