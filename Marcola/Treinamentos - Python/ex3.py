frase = input("")

frase.strip()
frase.lower()

concat = frase.replace(" ", "")

size = len(concat) 

flag = True
for i in range (int(size/2)):
    if concat[i] != concat[-(i+1)]:
        flag = False
        break

if flag:
    print("A frase É um palíndromo!")
else:
    print("A frase NÃO é um palíndromo.")