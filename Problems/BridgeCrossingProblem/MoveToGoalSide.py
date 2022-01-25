from IAction import IAction
from Sides import Sides

class MoveToGoalSide(IAction):
    def __init__(self):
        self.name = "Move To Goal Side"
    def apply(self, state):
        next_states = []
        if(state.side1[3]):
            if(state.side1[0] and state.side1[1]):
                next_state = Sides(-state.side1[0], -state.side1[1], state.side1[2], 0)
                next_states.append(next_state)
            if(state.side1[0] and state.side1[2]):
                next_state = Sides(-state.side1[0], state.side1[1], -state.side1[2], 0)
                next_states.append(next_state)
            if(state.side1[1] and state.side1[2]):
                next_state = Sides(state.side1[0], -state.side1[1], +state.side1[2], 0)
                next_states.append(next_state)
            if(state.side1[0] and not (state.side1[1] or state.side1[2])):
                next_state = Sides(-state.side1[0], state.side1[1], state.side1[2], 0)
                next_states.append(next_state)
            if(state.side1[1] and not (state.side1[0] or state.side1[2])):
                next_state = Sides(state.side1[0], -state.side1[1], state.side1[2], 0)
                next_states.append(next_state)
            if(state.side1[2] and not (state.side1[0] or state.side1[1])):
                next_state = Sides(state.side1[0], state.side1[1], -state.side1[2], 0)
                next_states.append(next_state)

        return next_states