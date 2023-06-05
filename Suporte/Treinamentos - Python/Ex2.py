"""
Exercicio 2 - Treinamento Python NRA- SEMEAR
Marco Soprani Tayar (Suporte)
"""

i = 1  # contagem de numeros
n = int(input("Digite o {}° número inteiro: ".format(i)))  # numero atual
s = n  # soma dos numeros
maior = n  # maior numero
menor = n  # menor numero

while True:
    r = input("Você deseja continuar escrevendo números? (S= Sim/ N= Não) ")
    if r == "N" or r == "n":
        break
    elif r == "S" or r == "s":
        i += 1
        n = int(input("Digite o {}° número inteiro: ".format(i)))  # numero atual
        s += n  # adiciona o numero a soma
        if n > maior:
            maior = n  # atualiza o maior numero
        if n < menor:
            menor = n  # atualiza o maior numero
    else:
        print("Digite uma resposta válida.")

media = float(s / i)  # media dos valores

print("A média dos {} valores é {:.2f}, sendo o maior {} e o menor {}.".format(i, media, maior, menor))
