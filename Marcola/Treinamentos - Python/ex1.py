dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos km foram rodados? "))

total = 60.0 * float(dias) + 0.15 * km
print("O Total a pagar é R$", format(total))