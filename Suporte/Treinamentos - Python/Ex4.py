"""
Exercicio 4 - Treinamento Python NRA SEMEAR
Marco Soprani Tayar (Suporte)
"""

time = []
total = 0


def adicionadados():
    nome = input('Digite o nome do jogador: ')
    quant = int(input('Digite o numero de jogos do jogador {}: '.format(nome)))
    jogador = {'nome': nome, 'quant': quant, 'total': ''}
    totjog = 0
    for i in range(quant):
        gol = int(input('Quantidade de gols na partida {}: '.format(i+1)))
        totjog += gol
    jogador['total'] = totjog
    return jogador, totjog


def adicionajogador(jogador):
    time.append(jogador)
    return


jog = adicionadados()
adicionajogador(jog[0])
total += int(jog[1])

while True:
    r = input("Você deseja continuar inscrevendo atletas? (S= Sim/ N= Não) ")
    if r == "N" or r == "n":
        break
    elif r == "S" or r == "s":
        jog = adicionadados()
        adicionajogador(jog[0])
        total += int(jog[1])

    else:
        print("Digite uma resposta válida.")

print(time)
print(total)
