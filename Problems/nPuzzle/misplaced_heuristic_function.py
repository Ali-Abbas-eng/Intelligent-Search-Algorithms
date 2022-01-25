from HeuristicFunction import HeuristicFunction


class Misplaces(HeuristicFunction):
    @property
    def goal_state(self):
        return self.__goal_state
    @goal_state.setter
    def goal_state(self, gs):
        self.__goal_state = gs

    def getH(self, state):
        misplaced = 0
        for i in range(state.board_size):
            for j in range(state.board_size):
                if(state.tiles[i][j] != self.goal_state.board[i][j]):
                    misplaced += 1
        return misplaced