def sum(n):
  if n < 2:
    return 1
  else:
    return 1/n + sum(n - 1)
n = eval(input("Give a number: "))
print(sum(n))