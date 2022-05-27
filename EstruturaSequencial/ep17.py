import math
area = int(input("Informe o tamanho da área a ser pintada: "))

litros = area/3
print("Litros de tinta:",round(litros,2),"litros")

latas = litros/18
print("Quantidades de latas de tinta:",math.ceil(latas))

preco1 = math.ceil(latas)*80.00
print("Preço total latas: R$",round(preco1,2))

galao = litros/3.6
print("Quantidades de galões de tinta:",math.ceil(galao))

preco2 = math.ceil(galao)*25.00
print("Preço total galão: R$",round(preco2,2))

