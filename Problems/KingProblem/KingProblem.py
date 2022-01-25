from GraphProblem import GraphProblem
from MoveToNextCity import MoveToNextCity
from GraphState import GraphState

class KingProblem(GraphProblem):
    @property
    def edited_graph(self):
        return self.__edited_graph
    @edited_graph.setter
    def edited_graph(self, eg):
        self.__edited_graph = eg

    @property
    def edition(self):
        return self.__edition
    @edition.setter
    def edition(self, e):
        self.__edition = e
    @property
    def graph(self):
        return self.__graph
    @graph.setter
    def graph(self, g):
        self.__graph = g

    def __init__(self, graph):
        self.graph = graph.adjacency_matrix
        self.initial_state = GraphState(the_graph = self.graph, size=graph.graph_size, current_state_index=graph.source)
        self.goal_state = GraphState(the_graph=graph.adjacency_matrix, size=graph.graph_size, current_state_index=graph.distination)
        self.graph_size = graph.graph_size
        self.actions = [MoveToNextCity()]

    def get_action_cost(self, state1, action, state2):
        return self.graph[state2.index][state1.index]