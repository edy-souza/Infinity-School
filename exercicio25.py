"""
Faça um programa que peça o tamanho de um arquivo para download em MB
(megabytes) e a velocidade de um link de Internet em Mbps (megabits por segundo),
calcule e informe o tempo aproximado de download do arquivo usando este link (em
minutos).
Obs: 1 MB = 8 Mb

"""

arquivo = int(input("Informe o tabanho do arquivo em MB (megabytes): "))
velocidade = int(input("Inofrme a velocidade em Mbps: (megabitis por segundo: ) "))
arquivo = (arquivo * 8)
velocidade = (arquivo / 60)

print(f"Tempo aproximado de download em minutos: {arquivo / 60:.2f} ")
