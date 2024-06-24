#iterando a lista
game_list = ['Gears of War', 'Halo', 'GTA', 'God of War']
for game in game_list:
    print(game)

print('-' * 5)
#outra forma
for i in range(len(game_list)):
    print(game_list[i])

print('-' * 5)
#com while

i = 0

while i < len(game_list):
    print(game_list[i])
    i = i + 1