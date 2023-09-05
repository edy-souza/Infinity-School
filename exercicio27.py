"""
Faça um programa que solicite ao usuário que digite seu nome e sua idade, e
exiba uma mensagem informando o ano em que ele completará 100 anos. Considere
que ela já fez aniversário em 2023.

"""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
ano = (2023 - idade + 100)
print(f"Você completará 100 anos em: {ano}")
