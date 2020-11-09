factorial_of_n = int(input("Enter for n: "))

for_fact = 1

for i in range(1, factorial_of_n+1):
  for_fact *= i

print(for_fact)