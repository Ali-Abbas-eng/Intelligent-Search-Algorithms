from SearchAlgorithm import SearchAlgorithm
from Node import Node
from queue import PriorityQueue

class GreedyBestFirstSearch(SearchAlgorithm):
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

    def __init__(self, use_graph_search):
        self.use_graph_search = use_graph_search
        self.frontier = PriorityQueue()
        self.explored = []
        self.visiting_order = 0
        self.developed_nodes = 0

    def search(self, problem):
        start_node = Node(problem.initial_state)
        while(self.frontier.not_empty):
            current_node = self.frontier.get()
            current_node.visiting_order = self.visiting_order + 1
            self.visiting_order += 1
            if(self.use_graph_search and current_node.state in self.explored):
                continue
            if(problem.is_goal(current_node.state)):
                return current_node
            self.explored.append(current_node.state)
            for action in problem.actions:
                self.next_states = action.apply(current_node.state)
                self.developed_nodes += len(self.next_states)
                for state in self.next_states:
                    action_cost = problem.get_action_cost(state, action, current_node.state)
                    path_cost = action_cost + current_node.get_path_cost()
                    total_estimated_cost = path_cost + problem.get_heuristic_function().getH(state)
                    child = Node(state = state, parent = current_node, action = action, path_cost = path_cost, total_cost = total_estimated_cost)
                    self.frontierl.put(child)




