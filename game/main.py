from game.engine import Engine
from game.map import a_map

if __name__ == '__main__':
    a_game = Engine(a_map)
    a_game.play()
