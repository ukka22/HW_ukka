
def plus(x,y): return x+y
def minus(x,y):return x-y
def prois(x,y):return x*y
def delen (x,y):
    if y==0:
        return "error"
    else:
        return x/y
while True:
    print("Введите 2 числа:")
    x = float(input("x="))
    s = input("введите знак операции (+,-,*,/), 0-выход:")
    y = float(input("y="))
    if s=="0":
        break
    else:
      if s == "+":
        print("решение:",plus(x,y))
      if s == "-":
        print("решение:", minus(x, y))
      if s == "*":
        print("решение:", prois(x, y))
      if s == "/":
        print("решение:", delen(x, y))
