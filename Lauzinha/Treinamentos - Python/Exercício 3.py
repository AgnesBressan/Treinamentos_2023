frase = ((str(input("Digite um frase:"))).lower()).replace(' ', '')
invertida = frase[::-1]
if invertida == frase:
    print("É palíndromo")
else:
    print("Não é palíndromo")
