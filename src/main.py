from Game import Game
from Player import Player

blue = "\x1b[1;37;44m"
red = "\x1b[1;33;41m"
clear = "\x1b[0m"


def main():
    p1 = Player("name1", "x")
    p2 = Player("name2", "o")

    game = Game(p1, p2)

    done = False
    turn = 1
    while not done:
        p = p1 if turn % 2 > 0 else p2

        print(red + f"turn: {turn} player: {p.name} token: {p.token} " + clear)
        play = input(
            blue + 'Where do you want to move? x y top left is "0 0": ' + clear
        )
        # split input into array
        plays = play.split(" ")
        # print(plays)
        if len(plays) != 2:
            print("bad format, skipping turn\n")
        else:
            print(game.move(int(plays[0]), int(plays[1]), p.token))

        ret = game.is_game_over()
        turn += 1
        if ret:
            print("winner: ", ret)
            done = True


main()
