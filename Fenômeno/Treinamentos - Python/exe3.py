#exercicio 3 treinamento semear python
# Thiago Goncalves

def palindromo (s):
    s = s.lower()
    s = ''.join(s.split())

    tam = len(s)
    inverted = ''

    for i in range (0, tam, 1):
        inverted = s[i] + inverted

    if inverted == s:
        print('eh palindromo')
    else:
        print('nao eh palindromo')

s = input('Digite a palavra a ser analisada: ')
palindromo(s)