current_date = input("Please enter the date: ")
current_month = str(input("Please enter the month: "))

# spring: march20, april, may
# summer: june21, july, august
# fall: september22, october, november
# winter: december21, january, february 

if current_month == "march":
  if current_date >= 20:
    print("Season is Spring ")
  elif current_month == "april" or current_month == "may":
    print("Season is Spring ")
  elif current_month == "june":
    if current_date < 21:
      print("Season is Spring")

# I got a bit confused at this point so I check solutions after lab sessions and share this for you to see what did I do in lesson 