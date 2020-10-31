from Game import Game
from Player import Player


def main():
    p1 = Player("name1", "x")
    p2 = Player("name2", "o")

    game = Game(p1, p2)

    ###
    print(game.move(1, 1, p1.token))


main()
