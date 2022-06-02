turno = str(input("Insira o turno que você estuda. \nM-matutino ou V-Vespertino ou N- Noturno: "))

if turno == "M":
  print("\nBom dia!")
  
elif turno == "V":
  print("\nBoa tarde!")
elif turno == "N":
  print("\nBoa noite!")
else:
  print("\nValor Inválido!")