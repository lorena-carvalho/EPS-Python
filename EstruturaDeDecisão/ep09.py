a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))

if (a < b and a < c):
  if(b < c):
    print("Ordem decrescente")
    print(c,b,a) 
  
  else:
    print("Ordem decrescente")
    print(b,c,a)  
    
elif(a > b and a > c):
  if(b < c):
    print("Ordem decrescente")
    print(a,c,b)
  else:
    print("Ordem decrescente")
    print(a,b,c)
  
elif(b < a and b < c):
  if(a < c):
    print("Ordem decrescente")
    print(c,a,b)
  else: 
    print("Ordem decrescente")
    print(a,c,b)
    
elif(b > a and b > c):
  if(a < c):
    print(b,c,a)
  else: 
    print(b,a,c)
    
elif(c < a and c < b):
  if(a < b):
    print(b,a,c)
  else:
    print(a,b,c)   
elif(c > a and c > b):
  if(a < b):
    print(b,a,c)
  else:
    print(a,b,c)
      
