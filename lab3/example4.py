ticket_price = 3

age = int(input("Please enter your age: "))

if age < 6 or age > 60:
  print("You have a free Ticket!")
elif age >= 6 and age <= 18:
  ticket_price = ticket_price*(1/2)
  print("Your ticket price is: ", float(ticket_price))
else:
  print("Your ticket price is: ", ticket_price)