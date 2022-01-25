from IAction import IAction
from WaterJugsState import WaterJugsState

class GlughGlugh(IAction):
    def __init__(self):
        self.name = "GlughGlugh"

    def pour(self, current_jug, goal_jug):
        available_space = goal_jug[1] - goal_jug[0]
        maximum_water_to_pour = min(current_jug[0], available_space)
        remaining_water = current_jug[0] - maximum_water_to_pour
        resulting_contained_water = goal_jug[0] + maximum_water_to_pour
        return ((remaining_water, current_jug[1]), (resulting_contained_water, goal_jug[1]))

    def apply(self, state):
        next_states = []

        for i in range(3):
            for j in range(3):
                jugs = state.jugs.copy()
                if(i == j):
                    continue
                jugs[i], jugs[j] = self.pour(jugs[i], jugs[j])
                next_states.append(WaterJugsState(jugs = jugs))
        for state in next_states:
            print(state)

        return next_states
