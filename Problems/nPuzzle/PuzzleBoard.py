from State import State


class PuzzleBoard(State):
    @property
    def tiles(self):
        return self.__tiles
    @tiles.setter
    def tiles(self, t):
        self.__tiles = t

    @property
    def board_size(self):
        return self.__board_size
    @board_size.setter
    def board_size(self, bs):
        self.__board_size = bs

    @property
    def mepty_i(self):
        return self.__empty_i
    @mepty_i.setter
    def emptyI(self, ei):
        self.__emptyI = ei

    @property
    def mepty_j(self):
        return self.__empty_j

    @mepty_j.setter
    def empty_j(self, ej):
        self.__empty_j = ej

    def __str__(self):
        s = ""
        for i in range(self.board_size):
            for j in range(self.board_size):
                s += self.tiles[i][j] + ' '
            s += '\n'

        return s

    def __eq__(self, another_state):
        for i in range(self.boardSize):
            for j in range(another_state.boardSize):
                if(not self.tiles[i][j] == another_state.tiles[i][j]):
                    return False
        return True

