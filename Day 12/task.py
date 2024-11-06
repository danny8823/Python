enemies = ['Skeleton', 'Zombie', 'Alien']
game_level = 3
message = 'testing'


def create_enemy():
    global message
    if game_level < 5:
        message += enemies[0]
        print(message)


create_enemy()
