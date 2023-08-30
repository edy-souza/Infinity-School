# Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))
n3 = int(input("Informe outro número: "))

if n1 == n2 == n3:
    print("Todos números iguais.")
elif n1 >= n2 and n1 >= n3:
    print(f"O maior número é: {n1}")
elif n2 >= n1 and n2 >= n3:
    print(f"O maior número é: {n2}")
else:
    print(f"O maior número é: {n3}")