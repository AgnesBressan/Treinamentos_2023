continuar = "S"
lista = []
while continuar == "S":
    n = int(input("Insira um número:"))
    lista.append(n)
    continuar = str(input("Deseja continuar? (Responda com S ou N)")).upper()

else:
    print(f"A média dos valores fornecidos foi: {(sum(lista))/(len(lista))}, O maior valor foi: {max(lista)}, O menor valor foi {min(lista)}")