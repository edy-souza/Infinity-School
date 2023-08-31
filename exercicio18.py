"""
Faça um programa que:
a) peça o primeiro nome e em seguida exiba: “Olá {nome}!”.
b) pergunte o sobrenome do usuário e exiba: “Como vai, {nome completo}?”.
c) Por fim, pergunte a idade do usuário e exiba: “Olá, Sr.(a) {sobrenome}, você
tem {idade} anos de idade.”

"""

nome = input("Qual é seu primeiro nome: ")
print(f"Olá {nome}!")

sobreNome = input("Qual é seu sobrenome: ")
print(f"Como vai, {nome} {sobreNome}?")

idade = input("Qual sua idade: ")
print(f"Olá, Sr.(a) {sobreNome}, você tem {idade} anos de idade.")
