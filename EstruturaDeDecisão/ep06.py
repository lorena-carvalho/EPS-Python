a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))

if (a > b and a > c):
  print("Maior número:",a)
elif(b > a and b > c):
  print("Maior número:",b)
elif(c > a and c > b):
  print("Maior número:",c)