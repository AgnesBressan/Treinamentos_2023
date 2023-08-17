#exercicio 4 treinamento semear python
# Thiago Goncalves

jogadores = []
aux = 's'
j = 0

while aux == 's':
    nome = input('digite o nome do jogador: ')
    partidas = int(input('digite o numero de partidas jogadas: '))

    soma = 0
    for i in range(1, partidas + 1, 1):
        gols = int(input('digite o numero de gols da partida {}: '.format(i)))
        soma = soma + gols

    print('o numero total de gols do jogador {} eh {}'.format(nome, soma))

    jogadores.insert(j, {'nome':nome, 'partidas':partidas, 'gols':soma})

    aux = input('se quiser adicionar mais alguem jogador digite s, se não digite n: ')
    if aux != 's' and aux != 'n':
        while aux != 's' and aux != 'n':
            aux = input('digito nao reconhecido pelo sistema, digite apenas s ou n: ')

somagols = 0
for i in range (0, len(jogadores), 1):
    print(jogadores[i])
    somagols = somagols + jogadores[i]['gols']

print('o numero total de gols do time eh: ', somagols)
