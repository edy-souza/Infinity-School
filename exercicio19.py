"""
Faça um programa que peça quatro notas bimestrais e mostre a média aritmética
e a média ponderada. Para realização da média ponderada, considere que a primeira
nota digitada tem peso 3, a segunda nota peso 2 e as terceira e quarta notas peso 1.

"""
b1 = int(input("Informe a nota do Bimestre 1: "))
b2 = int(input("Informe a nota do Bimestre 2: "))
b3 = int(input("Informe a nota do Bimestre 3: "))
b4 = int(input("Informe a nota do Bimestre 4: "))

print(f'Média Ponderada: {(b1*3 + b2*2 + b3*1 + b4*1) / 4}')
print(f"Média: {(b1 + b2 + b3 + b4) / 4}")
