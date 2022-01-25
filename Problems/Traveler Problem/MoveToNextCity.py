from IAction import IAction
from GraphState import GraphState
class MoveToNextCity(IAction):
    def __init__(self):
        self.name = "NotDefined"

    def apply(self, state):
        next_states = []
        row = state.the_graph[state.index]
        for column in range(len(row)):
            if(row[column] > 0 ):
                next_state = GraphState(the_graph = state.the_graph, size = state.graph_size, current_state_index = column)
                if(not next_state in next_states):
                    next_states.append(next_state)

        return next_states



