#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tam = int(input("Informe o tamanho do arquivo em MB: "))
vel = int(input("Informe a velocidade de um link de Internet em Mbps: "))

tempo = tam/vel

print("Tempo aproximado de download do arquivo:",tempo,"segundos")