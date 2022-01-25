import MoveToNextCity
import Problem
import GraphState

class GraphProblem(Problem.Problem):
    @property
    def graph_size(self):
        return self.__graph_size
    @graph_size.setter
    def graph_size(self, gs):
        self.__graph_size = gs

    def __init__(self):
        s = GraphState.GraphState()
        s.graph_size = 4
        s.grph_current_state_index = 0
        s.the_graph = [[0, 1, 1, 0],
                       [1, 0, 1, 0],
                       [1, 1, 0, 1],
                       [0, 0, 1, 0]]
        self.initial_state = s
        temp = GraphState.GraphState(the_graph = s.the_graph, size =s.graph_size, current_state_index =s.graph_size - 1)
        self.goal_state = temp

    def __init__(self, graph):
        self.initial_state = GraphState.GraphState(the_graph = graph.adjacency_matrix, size = graph.graph_size, current_state_index = graph.source)
        self.goal_state = GraphState.GraphState(the_graph = graph.adjacency_matrix, size = graph.graph_size, current_state_index = graph.distination)
        self.graph_size = graph.graph_size
        self.actions = [MoveToNextCity.MoveToNextCity()]
    def is_goal(self, state):
        return state == (self.goal_state)

    def get_action_cost(self, state1, action, state2):
        return state1.the_graph[state1.index][state2.index]
