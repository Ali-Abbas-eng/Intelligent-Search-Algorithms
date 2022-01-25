from HeuristicFunction import HeuristicFunction


class Manhatin (HeuristicFunction):
    @property
    def goal_state(self):
        return self.__goal_state
    @goal_state.setter
    def goal_state(self, gs):
        self.__goal_state = gs

    def getH(self, state):
        manhatn = 0
        for i in range(state.boardSize):
            for j in range(state.boardSize):
                for k in range(state.boardSize):
                    for m in range(state.boardSize):
                        if(state.tiles[i][j] == self.goal_state.tiles[k][m]):
                            manhatn += (abs((i - k))) + (abs(j - m))

        return manhatn