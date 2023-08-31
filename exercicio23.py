"""
Faça um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
A fórmula é:

IMC = peso / altura²

"""
peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

print("Seu indíce de massa corporal é: " f"{peso / altura**2:.2f}")
