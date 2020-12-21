
def countdown(n):
  if n == 0 :
    print("Alert!")
  else:
    print(n)
    countdown(n-1)
n = eval(input("How many seconds left ?"))
countdown(n)