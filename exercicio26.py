"""
Faça um programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. Sabendo
que são descontados 11% para o Imposto de Renda (IR), 8% para o INSS e 5% para
o sindicato, faça um programa que nos dê:

1. salário bruto.
2. quanto pagou ao INSS.
3. quanto pagou ao sindicato.
4. o salário líquido.

"""
contador = 1
while contador <= 3:

    preco_hora = float(input("Informe quanto você ganha por hora: "))
    hora_mes = float(input("Informe o Total de horas trabalhadas no mês: "))

    descontos = (preco_hora * hora_mes * 0.24)
    salario_liquido = (preco_hora * hora_mes - descontos)

    print(f"Salario Bruto R$: {preco_hora * hora_mes:.2f}")
    print(
        f"Quanto pagou de Imposto de Renda R$: {preco_hora * hora_mes * 0.11:.2f} ")
    print(f"Quanto pagou ao INSS R$: {preco_hora * hora_mes * 0.08:.2f}")
    print(f"Quanto pagou ao Sindicato: R$: {preco_hora * hora_mes * 0.05:.2f}")
    print(f"Salário Líquido R$: {salario_liquido:.2f}")

    contador += 1
