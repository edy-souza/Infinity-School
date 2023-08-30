# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")

if letra.isalpha() and len(letra) == 1:
    if letra.lower() in 'aeiou':
        print("A letra digitada é uma vogal.")
    else:
        print("A letra digitada é uma consoante.")
else:
    print("Por favor, digite apenas uma letra.")


# .isalpha()  verifica se a entrada do input é realmente uma letra
# e se possui apenas um caractere (usando len(letra) == 1).
# verificamos se a letra (convertida para minúscula com letra.lower())
# está la lista de vogais ()"aeiou")
