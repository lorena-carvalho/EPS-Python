n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

media = (n1+n2)/2

print("Média: ", media)

if(7 <= media < 10) :
  print("Aprovado")
elif(media == 10):
  print("Aprovado com distinção")
else:
  print("Reprovado")