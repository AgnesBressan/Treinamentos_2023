jogadores = [] # lista que armazenará todos os dados

# cada elemento da lista será uma tupla
# Nome, Partidas, lista[]

while True: 

    nome = input("Digite o nome do jogador: ")

    partidas = int(input("Digite quantas partidas ele jogou: "))

    print("Digite a quantidade de gols em cada partida: ")
    gols = []
    for i in range (partidas):
        g = int(input(""))
        gols.append(g)
        
    tupla = (nome, partidas, gols)
    jogadores.append(tupla)

    print("\nDeseja adicionar mais jogadores? s/n")

    flag = input()
    
    if flag == 's':
        print("\n")
        continue
        
    else:
        break

print("\n")

for i in range(len(jogadores)):
    print("{}, {} partidas e {} gols".format(jogadores[i][0], jogadores[i][1], sum(jogadores[i][2])))

totalGols = 0
for i in range(len(jogadores)):
    totalGols += sum(jogadores[i][2])

print("Total de gols da equipe:", totalGols)