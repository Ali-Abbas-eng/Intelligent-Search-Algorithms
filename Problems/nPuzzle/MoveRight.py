from OLD import IAction
import PuzzleBoard


class MoveRight(IAction.IAction):
    @property
    def get_name(self):
        return "Move Right"

    def apply(self, state):
        next_states = []
        new_tiles = []
        for i in range(state.board_size):
            for j in range(state.board_size):
                new_tiles = state.tiles[i][j]

        if (state.empty_j > 0):
            new_tiles[state.empty_i][state.empty_j] = new_tiles[state.empty_i][state.empty_j + 1]
            new_tiles[state.empty_i][state.empty_j + 1] = 0
            next_state = PuzzleBoard.PuzzleBoard()
            next_state.tiles = new_tiles
            next_state.board_size = state.board_size
            next_state.empty_i = state.empty_i
            next_state.empty_j = state.empty_j + 1
            next_states.append(next_state)

        return next_states