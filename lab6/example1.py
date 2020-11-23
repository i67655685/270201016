main_mail = "ceng113@example.com"

mail_adress = input("Please enter your e-mail adress: ")

if mail_adress.upper() == main_mail.upper():
  print(True)
elif mail_adress.lower() == main_mail.lower():
  print(True)

#I cant get the dots problem before "@" sign