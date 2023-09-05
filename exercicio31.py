"""
Faça um programa que solicite ao usuário um número real e exiba apenas a parte
decimal desse número, por exemplo:
• Entrada: 7.43.
• Saída: 43.

"""

numero_real = float(input("Informe um número real: "))
parte_decimal = numero_real - int(numero_real)
parte_decimal *= 100  # Multiplica por 100 para obter duas casas decimais
print(f"Saída: {int(parte_decimal):03d}")
