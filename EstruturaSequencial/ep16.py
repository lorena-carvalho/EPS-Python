import math
area = int(input("Informe o tamanho da área a ser pintada: "))

litros = area/3
print("Litros de tinta:",round(litros,2),"litros")

latas = litros/18
print("Quantidades de latas de tinta:",math.ceil(latas))

preco = math.ceil(latas)*80.00
print("Preço total: R$",round(preco,2))
