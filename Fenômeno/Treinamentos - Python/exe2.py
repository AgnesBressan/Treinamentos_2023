#exercicio 2 treinamento semear python
# Thiago Goncalves

soma = 0
x = 's'

n = int(input('digite um numero: '))
x = input('se quiser continuar digite s, se não digite n: ')

if x != 's' and x != 'n':
    while x != 's' and x != 'n':
        x = input('digito nao reconhecido pelo sistema, digite apenas s ou n: ')

soma = soma + n
maior = n
menor = n

while x == 's':
    n = int(input('digite um numero: '))
    x = input('se quiser continuar digite s, se não digite n: ')

    if x != 's' and x != 'n':
        while x != 's' and x != 'n':
            x = input('digito nao reconhecido pelo sistema, digite apenas s ou n: ')

    soma = soma + n

    if maior < n :
        maior = n

    if menor > n :
        menor = n

print('Soma: ', soma)
print('Menor: ', menor)
print('Maior: ', maior)


