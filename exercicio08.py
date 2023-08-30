# Faça um Programa que peça as 4 notas bimestrais e mostre a
# média ponderada em que as notas terão, respectivamente, os
# seguintes pesos: 2, 4, 3, 1.

b1 = float(input("Digite a nota do bimestre 1: "))
b2 = float(input("Digite a nota do bimestre 2: "))
b3 = float(input("Digite a nota do bimestre 3: "))
b4 = float(input("Digite a nota do bimestre 4: "))

media_ponderada = (b1*2 + b2*4 + b3*3 + b4*1) / 4

print(f"A média ponderada referente aos 4 bimestre foi:", media_ponderada)
