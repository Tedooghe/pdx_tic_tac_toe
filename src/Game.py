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

    def move(self, x, y, player):
        if self.board[x + 3 * y] != " ":
            print(" seats taken ")
            return
        self.board[x + 3 * y] = player
        self.turn += 1
        # return self.calc_winner()
        return self.__repr__()

    def winLineCheck(self, pos, n):
        if (
            self.board[pos] == self.board[pos + n]
            and self.board[pos + n] == self.board[pos + 2 * n]
        ):
            return self.board[pos]

    def horiCheck(self):
        for pos in [0, 3, 6]:
            if self.winLineCheck(pos, 1):
                return self.board[pos]

    def vertCheck(self):
        for pos in range(3):
            if self.winLineCheck(pos, 3):
                return self.board[pos]

    def diagCheck(self):
        return self.winLineCheck(0, 4) or self.winLineCheck(2, 2)

    def calc_winner(self):
        if self.turn < 5:
            return
        return self.horiCheck() or self.vertCheck() or self.diagCheck()

    def is_full(self):
        return self.turn > 8

    def is_game_over(self):
        return self.calc_winner() or self.board.count(" ") == 0


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
