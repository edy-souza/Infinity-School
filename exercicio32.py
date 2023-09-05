"""
Faça um programa que solicite ao usuário que digite um número e exiba a tabuada
desse número (multiplicação de 1 a 10).

"""

numero = int(input("Digite um número: "))

for mult in range(1, 11):
    resultado = numero * mult
    print(f"{numero} x {mult} = {resultado} ")
