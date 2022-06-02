a = float(input("Produto 1: R$ "))
b = float(input("Produto 2: R$ "))
c = float(input("Produto 3: R$ "))

if (a < b and a < c):
  print("Produto mais barato: R$",a)
elif(b < a and b < c):
  print("Produto mais barato: R$",b)
elif(c < a and c < b):
  print("Produto mais barato: R$",c)