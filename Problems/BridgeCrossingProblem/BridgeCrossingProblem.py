from Problem import Problem
from MoveToGoalSide import MoveToGoalSide
from RetrunTheLight import ReturnTheLight
import numpy as np

class BridgeCrossingProblem(Problem):
    @property
    def weights(self):
        return self.__weights
    @weights.setter
    def weights(self, w):
        self.__weights = w
    def __init__(self, initial_state, goal_state):
        self.weights = initial_state.side1
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = [MoveToGoalSide(), ReturnTheLight()]
    def absolut(self, arg):
        for i in range(len(arg)):
            if (arg[i] < 0):
                arg[i] *= -1
        return arg

    def get_action_cost(self, state1, action, state2):
        cost = [0] * (len(state1.side1) - 1)
        for i in range(len(state1.side1) - 1):
            cost[i] =  state1.side1[i] - state2.side1[i]

        return (max(self.absolut(cost)) / 2)

    def is_goal(self, state):
        for p in state.side1:
            if(p > 0):
                return False
        return True
    def solv(self, search_algorithm):
        return search_algorithm.search(self)

