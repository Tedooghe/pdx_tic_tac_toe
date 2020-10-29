

class Game():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.board = [" " for _ in range(9)]

    def __repr__(self):
        return "".join([self.board[x] + "|" if x % 3 > 0 else "\n" for x in range(9)])

g = Game("a", "b")
print(g)