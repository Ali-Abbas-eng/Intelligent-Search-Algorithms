from Problem import Problem
from WaterJugsState import WaterJugsState
from GlughGlugh import GlughGlugh

class WaterJugsProblem(Problem):
    @property
    def initial_state(self):
        return self.__initial_state
    @initial_state.setter
    def initial_state(self, init_st):
        self.__initial_state = init_st

    def __init__(self, initial_state = [(8, 8), (0, 5), (0, 3)], goal = 4):
        self.initial_state = WaterJugsState(initial_state)
        self.actions = [GlughGlugh()]
        self.goal_state = 4

    def is_goal(self, state):
        for jug in state.jugs:
            if(jug[0] == self.goal_state):
                return True
        return False