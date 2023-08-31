"""
Faça um programa que peça a temperatura em graus Celsius, transforme e
mostre a temperatura em graus Fahrenheit. A fórmula para a conversão é: F = 9/5 C +
32.

"""
C = float(input("Infome a temperatura em graus Celsius: "))

print("Temperatura em Graus Fahrenheit: ", f"{C * 9/5 + 32:.2f}")
