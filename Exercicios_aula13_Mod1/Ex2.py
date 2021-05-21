nome = input("Digite o nome do jogador: ").title()
partidas = int(input("Digite a quantidade de partidas que ele jogou: "))

gols_partida = []

#for jogo in range(1, partidas+1) : 
    #gols_partida.append(int(input(f"Quantos gols foram feitos na partida {jogo}: ")))
    #ou
for jogo in range(partidas):
    gols_partida.append(int(input(f"Quantos gols foram feitos na partida {jogo+1}: ")))
print(gols_partida)
print(f"O total de gol(s) feitos pelo jogador {nome} em {partidas} partida(s) no campeonato foi {sum(gols_partida)}.")

total_gols = sum(gols_partida)
print("Nome:", nome)
print("Partidas:", partidas)
print("Lista de gols:", gols_partida)
print("Total de gols:", total_gols)

#dicionario = dict() ou
#dicionario = {}
dicionario = {"Nome":nome, "Partidas":partidas, "Gols_partida":gols_partida, "Total_gols":total_gols}

print(f'O jogador {dicionario["Nome"]} jogou {dicionario["Partidas"]} partida(s) marcando {dicionario["Gols_partida"]} gol(s), e com um total de {dicionario["Total_gols"]} gols')
