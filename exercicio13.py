# Faça um programa que pergunte o preço de três produtos e
# informe qual produto você deve comprar, sabendo que a decisão
# é sempre pelo mais barato.

n1 = float(input("Informe o preço do arroz: "))
n2 = float(input("Informe o preço do feijão: "))
n3 = float(input("Informe o preço da carne: "))

if n1 == n2 == n3:
    print("Todos o preços são iguais.")
elif n1 <= n2 and n1 <= n3:
    print(f"O mais barato é arroz, pelo preço de: {n1:.2f}")
elif n2 <= n1 and n2 <= n3:
    print(f"O mais barato é feijão, pelo preço de: {n2:.2f}")
else:
    print(f"O mais barato é carne, pelo preço de: {n3:.2f}")
