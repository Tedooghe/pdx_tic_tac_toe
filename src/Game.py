class Game:
    def __init__(self, p1, p2):
        self.players = [p1, p2]
        self.board = [" " for _ in range(9)]
        self.turn = 0

    def __repr__(self):
        # return "\n" + "".join(
        #     [
        #         self.board[x] + "|" if x % 3 < 2 else self.board[x] + "\n"
        #         for x in range(9)
        #     ]
        # )
        ret = ["\n"]
        for x in range(9):
            if x % 3 < 2:
                ret.append(self.board[x] + "|")
            else:
                ret.append(self.board[x] + "\n")
        return "".join(ret)

    def move(self, x: int, y: int, player):
        # convert flat array to 2d 3x3
        pos = x + 3 * y
        if pos > len(self.board):
            print(" out of range ")
            return None
        # check if place on board is taken
        if self.board[pos] != " ":
            print(" seats taken ")
            return None
        self.board[pos] = player
        self.turn += 1
        # return self.calc_winner()
        return self.__repr__()

    def winLineCheck(self, i: int, n: int):
        # traverse board from index by n-size steps
        if (
            self.board[i] == self.board[i + n]
            and self.board[i + n] == self.board[i + 2 * n]
        ):
            return self.board[i]

    def horiCheck(self):
        # check for horizontal wins
        for i in [0, 3, 6]:
            if self.winLineCheck(i, 1):
                return self.board[i]

    def vertCheck(self):
        # check for vertical wins
        for i in range(3):
            if self.winLineCheck(i, 3):
                return self.board[i]

    # check for diagonal wins
    # from top left and top right
    def diagCheck(self):
        return self.winLineCheck(0, 4) or self.winLineCheck(2, 2)

    # check if minimum to win turns have been taken
    # return winner or None
    def calc_winner(self):
        if self.turn < 5:
            return
        return self.horiCheck() or self.vertCheck() or self.diagCheck()

    def is_full(self):
        return self.turn > 8

    # check winner or no spaces left
    def is_game_over(self):
        return self.calc_winner() or self.is_full()


def testy():
    g = Game("a", "b")
    print(g.move(1, 1, "b"), g.move(0, 1, "a"), g.move(2, 1, "a"))
    print(g.is_game_over())
    print(g.move(0, 0, "b"), g.move(1, 0, "b"), g.move(2, 0, "a"))
    print("full ", g.is_full(), "winner ", g.calc_winner(), "over ", g.is_game_over())
    print(g.move(2, 2, "b"), g.move(0, 2, "a"), g.move(1, 2, "c"))
    print("full ", g.is_full(), "winner ", g.calc_winner(), "over ", g.is_game_over())
    print(g)


testy()