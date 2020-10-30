class Game:
    def __init__(self, p1, p2):
        self.players = [p1, p2]
        self.board = [" " for _ in range(9)]
        self.turn = 0

    def __repr__(self):
        # return "".join(
        #     [
        #         self.board[x] + "|" if x % 3 < 2 else self.board[x] + "\n"
        #         for x in range(9)
        #     ]
        # )
        ret = []
        for x in range(9):
            if x % 3 < 2:
                ret.append(self.board[x] + "|")
            else:
                ret.append(self.board[x] + "\n")
        return ret

    def move(self, x, y, player):
        if self.board[x + 3 * y] != " ":
            print(" seats taken ")
            return
        self.board[x + 3 * y] = player
        self.turn += 1
        return self.calc_winner()

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
            if self.winLineCheck(pos, 1):
                return self.board[pos]

    def diagCheck(self):
        return self.winLineCheck(0, 4) or self.winLineCheck(2, 2)

    def calc_winner(self):
        if self.turn < 5:
            return
        return self.horiCheck() or self.vertCheck()


def testy():
    g = Game("a", "b")
    print(g.move(1, 1, "a"), g.move(0, 1, "a"), g.move(2, 1, "a"))
    print(g.move(0, 0, "b"), g.move(1, 0, "b"), g.move(2, 0, "b"))
    print(g)
