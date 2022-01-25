from OLD import Problem
import SeeAllPossibilities
class EightPuzzleProblem(Problem.Problem):

    def __init__(self, initial_state, goal_state):
        self.actions = []
        self.initial_state = initial_state
        self.goal_state = goal_state

    @property
    def goal_state(self):
        return self.__goal_state
    @goal_state.setter
    def goal_state(self, gs):
        self.__goal_state = gs


    def is_goal(self, state):
        return (state == self.goal_state)

    def get_actions(self):
        available_moves = SeeAllPossibilities.SeeAllPossibilities(state)
        for state in available_moves.next_states:
            self.actions.append(state)
