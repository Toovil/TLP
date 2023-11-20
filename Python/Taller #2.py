import pandas as pd
datos_jugadores = pd.read_csv("NBA_2024_per_game.csv", sep=",")

#1. Encontrar el jugador que mas tiempo haya jugado en la temporada.


max_tiempo = []

for i in datos_jugadores["MP"]:
    max_tiempo.append(i)
    
print(f'\n{datos_jugadores[datos_jugadores["MP"] == max(max_tiempo)]}')

print("\n///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n")

# 2.  Encontrar todos los jugadores que hayan jugado para los Cleveland Cavaliers (CLE) en la posición de Point Guard (PG).

print(datos_jugadores[(datos_jugadores["Tm"] == "CLE") & (datos_jugadores["Pos"] == "PG")])

print("\n///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n")

# 3. Encontrar los jugadores que tengan mas de 1 robo por partido (STL) y mas de 1 bloqueo por partido (BLK) usando list comprehension.

#print(datos_jugadores)

robos_bloqueos = [
    player for _, player in datos_jugadores.iterrows()
    if (player['STL'] > 1 and player['BLK'] > 1)
]

print([i['Player'] for i in robos_bloqueos])


print("\n///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n")

#4. Encontrar cual es el porcentaje de canastas de 3 puntos (3P%) se hacen en la liga.

print(round(100 * datos_jugadores['3P%'].mean()))

print("\n///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n")

#5.  Encontrar que jugadores estuvieron en 2 equipos o mas en una sola temporada.

print(datos_jugadores[datos_jugadores["Player"].duplicated()])


