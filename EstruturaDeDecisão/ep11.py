sal= float(input("Informe o salário: R$ "))

if sal <= 280:
  print("Salário antes do reajuste: R$",sal)
  print("Percentual de aumento aplicado: 20%")
  novo = sal*0.2
  print("Valor do aumento: R$",novo)
  print("Novo salário após o aumento: R$",sal+novo)

elif 280 < sal <= 700:
  print("Salário antes do reajuste: R$",sal)
  print("Percentual de aumento aplicado: 15%")
  novo = sal*0.15
  print("Valor do aumento: R$",novo)
  print("Novo salário após o aumento: R$",sal+novo)

elif 700 < sal <= 1500:
  print("Salário antes do reajuste: R$",sal)
  print("Percentual de aumento aplicado: 10%")
  novo = sal*0.1
  print("Valor do aumento: R$",novo)
  print("Novo salário após o aumento: R$",sal+novo)

elif sal > 1500:
  print("Salário antes do reajuste: R$",sal)
  print("Percentual de aumento aplicado: 5%")
  novo = sal*0.05
  print("Valor do aumento: R$",novo)
  print("Novo salário após o aumento: R$",sal+novo)