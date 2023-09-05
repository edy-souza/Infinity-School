"""
Faça um programa que solicite ao usuário o valor mensal do salário e reajuste a
remuneração em 8%.

"""

salario = float(input("Qual o valor do seu salário: "))
salario = (salario * 0.08 + salario)

print(f"Salário + reajuste de 8%: {salario:.2f}")
