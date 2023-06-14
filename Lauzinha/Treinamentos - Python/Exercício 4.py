start = (input("Deseja adicionar um jogador? (S/N) ")).upper()
infos = []
final = []
while start == "S":
    j = input("Nome do jogador: ")
    p = int(input(f"Quantas partidas {j} jogou? "))
    gols = []
    for i in range(p):
        g = int((input(f"Quantos gols na partida {i+1}? ")))
        gols.append(g)
    total = sum(gols)
    jogador = [j, gols, total]
    infos.append(jogador)
    final.append(jogador[2])
    start = (input("Deseja continuar? (S/N) ")).upper()

for i in range(int(len(infos))):
    print(f"Jogador: {infos[i][0]}")
    print(f"Gols por partida: {infos[i][1]}")
    print(f"Total de gols: {infos[i][2]}")

print(f"Total de gols do time: {sum(final)}")
