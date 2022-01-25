from IAction import IAction
from GraphState import GraphState

class Move(IAction):
    def __init__(self):
        self.name = "Move"

    def apply(self, state):
        graph = state.the_graph
        size = state.graph_size
        next_states = []
        row = state.index
        for column in range(size):
            if(graph[row][column]):
                state = GraphState(current_state_index = column, the_graph = graph, size = size)
                next_states.append(state)
            if(graph[column][row]):
                state = GraphState(current_state_index = column, the_graph = graph, size = size)
                next_states.append(state)
        return next_states
