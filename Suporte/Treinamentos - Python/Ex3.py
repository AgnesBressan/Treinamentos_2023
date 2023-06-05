"""
Exercicio 3 - Treinamento Python NRA- SEMEAR
Marco Soprani Tayar (Suporte)
"""

frase = input("Digite a frase")  # frase recebida


def ispalindrome(t):
    t = t.lower()
    t = t.strip()
    lista = t.split(' ')  # separa a partir dos espacos
    t = "".join(lista)  # junta sem os espacos
    n = int(len(t) / 2)  # analisa metade do comprimento da string
    if t[:n] == t[:-n-1:-1]:  # compara a metade inicial e o inverso da final
        print("É palíndromo!")
    else:
        print("Não é palíndromo :(")
    return


ispalindrome(frase)
