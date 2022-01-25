import State


class GraphState(State.State):
    @property
    def graph_size(self):
        return self.__graph_size
    @graph_size.setter
    def graph_size(self, gs):
        self.__graph_size = gs

    @property
    def index(self):
        return self.__index
    @index.setter
    def index(self, index):
        self.__index = index

    @property
    def the_graph(self):
        return self.__the_graph
    @the_graph.setter
    def the_graph(self, tg):
        self.__the_graph = tg

    def __init__(self, the_graph = None, current_state_index = None, size = None):
        self.the_graph = the_graph
        self.graph_size = size
        self.index = current_state_index

    def is_goal(self):
        return self.index == 3

    def __eq__(self, ot_gs):
        return (self.index == ot_gs.index)

    def __str__(self):
        return (f"State: {self.index}")



