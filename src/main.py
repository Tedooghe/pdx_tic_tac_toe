from Game import Game
from Player import Player


def main():
    p1 = Player("name1", "x")
    p2 = Player("name2", "o")

    game = Game(p1, p2)

    done = False
    turn = 1
    while not done:
        p = p1 if turn % 2 > 0 else p2

        print("Turn: ", p.name)
        play = input("Where do you want to move? x y top left is 0 0: ")
        # split input into array
        plays = play.split(" ")
        # print(plays)
        print(game.move(int(plays[0]), int(plays[1]), p.token))

        ret = game.is_game_over()
        turn += 1
        if ret:
            print("winner: ", ret)
            done = True


main()
