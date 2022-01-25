from queue import PriorityQueue
from SearchAlgorithm import SearchAlgorithm
from Node import Node

class UCS(SearchAlgorithm):
    @property
    def frontier(self):
        return self.__frontier
    @frontier.setter
    def frontier(self, f):
        self.__frontier = f

    @property
    def explored(self):
        return self.__explored
    @explored.setter
    def explored(self, e):
        self.__explored = e

    @property
    def next_states(self):
        return self.__next_states
    @next_states.setter
    def next_states(self, ns):
        self.__next_states = ns

    @property
    def visiting_order(self):
        return self.__visiting_order
    @visiting_order.setter
    def visiting_order(self, vo):
        self.__visiting_order = vo

    def __init__(self, use_graph_search = False):
        self.use_graph_search = use_graph_search
        self.frontier = PriorityQueue()
        self.explored = []
        self.next_states = []
        self.visiting_order = 0
        self.developed_nodes = 0

    def search(self, problem):
        start_node = Node(state = problem.initial_state, parent = None)
        self.frontier.put((0, start_node))

        while(not self.frontier.empty()):
            current_node = self.frontier.get()[1]
            current_node.visiting_order += self.visiting_order + 1
            self.visiting_order += 1
            if(self.use_graph_search and current_node.state in self.explored):
                continue

            if(problem.is_goal(current_node.state)):
                return current_node

            self.explored.append(current_node.state)
            for action in problem.actions:
                self.next_states = action.apply(current_node.state)
                self.developed_nodes += len(self.next_states)
                counter = 0
                for state in self.next_states:
                    action_cost = problem.get_action_cost(current_node.state, action, state)
                    path_cost = action_cost + current_node.path_cost
                    child = Node(state = state, parent =  current_node, action = action, path_cost = path_cost)
                    self.frontier.put((path_cost, child))
                    counter += 1
        return None
    