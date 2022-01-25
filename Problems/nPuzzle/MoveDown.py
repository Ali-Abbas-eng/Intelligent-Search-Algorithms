from OLD import IAction
from PuzzleBoard import PuzzleBoard


class MoveDown(IAction.IAction):
    @property
    def get_name(self):
        return "Move Down"

    def apply(self, state):
        next_states = []
        new_tiles = []
        for i in range(state.board_size):
            for j in range(state.board_size):
                new_tiles = state.tiles[i][j]

        if (state.empty_i < state.board_size - 1):
            new_tiles[state.empty_i][state.empty_j] = new_tiles[state.empty_i + 1][state.empty_j]
            new_tiles[state.empty_i + 1][state.empty_j] = 0
            next_state = PuzzleBoard()
            next_state.tiles = new_tiles
            next_state.board_size = state.board_size
            next_state.empty_i = state.empty_i + 1
            next_state.empty_j = state.empty_j
            next_states.append(next_state)

        return next_states