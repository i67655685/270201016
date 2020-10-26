students_gpa = float(input("Please enter your GPA: "))
number_of_lectures = int(input("Please enter number of lectures: "))

if students_gpa < 2.0 and number_of_lectures < 47:
  print("Not enough number of lectures and GPA!")
elif students_gpa < 2.0 and number_of_lectures >= 47:
  print("Not enough GPA!")
elif students_gpa >= 2.0 and number_of_lectures < 47:
  print("Not enough number of lectures!")
else :
  print("GRADUATED!")