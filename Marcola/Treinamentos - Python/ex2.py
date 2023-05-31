media = 0

while(True):

    print("Escreva 10 valores inteiros:")

    for i in range(10):

        x = int(input(""))
        media += x

        if i == 0:
            maior = x
            menor = x

        else:
            if maior < x:
                maior = x
            if menor > x:
                menor = x

    media /= 10

    print("\nMaior valor:", maior)
    print("Menor valor:", menor)
    print("Média dos valores:", media)

    print("\nDeseja continuar digitando valores? s/n")

    flag = input()
    
    if flag == 's':
        continue
    else:
        break
    