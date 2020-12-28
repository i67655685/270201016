n = int(input("Hailstone calculator:"))
def hailstone(n):
  print(n)
  if n > 1:
    if n % 2 == 0:
      print(hailstone(n / 2)) 
    else:
      print(hailstone((n * 3) + 1))
print(hailstone(n))