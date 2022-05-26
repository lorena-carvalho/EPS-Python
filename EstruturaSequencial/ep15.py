valor = int(input("Ganho por horas trabalhadas: ")) 
hora = int(input("Número de horas trabalhadas: "))

sal = valor*hora*30
print("+ Salário Bruto : R$",sal)

ir = sal*0.11
print("- IR (11%) : R$",round(ir,2))

inss = (sal-ir)*0.08
print("- INSS (8%) : R$",round(inss,2))

sind = (sal-ir-inss)*0.05
print("- Sindicato (5%) : R$",round(sind,2))

sal_liq = sal - ir - inss - sind
print("= Salário Liquido : R$",round(sal_liq,2))