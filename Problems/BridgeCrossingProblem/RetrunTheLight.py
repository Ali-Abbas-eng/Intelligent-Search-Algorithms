from IAction import IAction
from Sides import Sides

class ReturnTheLight(IAction):
    def __init__(self):
        self.name = "Return The Light"
    def apply(self, state):
        next_states = []
        if(state.side2[3]):
            if(state.side2[0]):
                next_state = state
                next_state.side2[0] *= -1
                next_state.side1[0] *= -1
                next_state.side2[3] = 0
                next_state.side1[3] = 1
                next_states.append(next_state)
            if(state.side2[1]):
                next_state = state
                next_state.side2[1] *= -1
                next_state.side1[1] *= -1
                next_state.side2[3] = 0
                next_state.side1[3] = 1
                next_states.append(next_state)
            if (state.side2[2]):
                next_state = state
                next_state.side2[2] *= -1
                next_state.side1[2] *= -1
                next_state.side2[3] = 0
                next_state.side1[3] = 1
                next_states.append(next_state)
        return next_states