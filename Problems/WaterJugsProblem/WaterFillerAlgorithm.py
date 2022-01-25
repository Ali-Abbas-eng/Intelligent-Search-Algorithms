from SearchAlgorithm import SearchAlgorithm
from Node import Node
from queue import Queue

class WaterFiller(SearchAlgorithm):
    @property
    def frontier(self):
        return self.__frontier
    @frontier.setter
    def frontier(self, f):
        self.__frontier = f

    def __init__(self):
        self.frontier = Queue()
        self.explored = []

    @property
    def next_states(self):
        return self.__next_states
    @next_states.setter
    def next_states(self, ns):
        self.__next_states = ns

    @property
    def explored(self):
        return self.__explored
    @explored.setter
    def explored(self, e):
        self.__explored = e

    def search(self, problem):
        start_node = Node(state = problem.initial_state, parent = None, path_cost = 0)
        self.frontier.put(start_node)
        self.next_states = []
        self.explored.append(start_node.state)

        while(not self.frontier.empty()):
            current_node = self.frontier.get()
            if(problem.is_goal(current_node.state)):
                return current_node
            for action in problem.actions:
                self.next_states = action.apply(current_node.state)
                for state in self.next_states:
                    if(state in self.explored):
                        continue
                    child = Node(state = state, parent = current_node)
                    self.frontier.put(child)
                    self.explored.append(state)
                break
        return None