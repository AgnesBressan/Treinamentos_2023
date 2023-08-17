#exercicio 1 treinamento semear python
# Thiago Goncalves

dias = int(input('Por quantos dias o carro foi alugado?'))
km = float(input('Qual a quantidade de quilômetro rodados por esse carro?'))

s1 = 60 * dias
s2 = 0.15 * km
total = s1 + s2

print('O preço total eh:', total)