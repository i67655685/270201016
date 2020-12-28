def mult(n, m):
  n = 3
  if m == 0:
    return 0
  elif m < 0:
    return - (n - mult(n, m+1))
  else:
    return n + mult(n, m-1)
print(mult(3,6))