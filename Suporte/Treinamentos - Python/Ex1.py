"""
Exercicio 1 - Treinamento Python NRA- SEMEAR
Marco Soprani Tayar (Suporte)
"""

d = int(input("Por quantos dias o carro foi alugado? "))  # numero de dias
km = float(input("Quantos km foram percorridos com o carro? "))  # distancia percorrida

p = d * 60 + 0.15 * km  # preco final

print("O valor a pagar é: R${:.2f}".format(p))
