from Node import Node
from SearchAlgorithm import SearchAlgorithm


class HillClimbing(SearchAlgorithm):
    def search(self, p):
        current_node = p.initial_state
        while(True):
            current_node.total_cost = p.getHeuristicFunction().getH(p.initial_state)
            best_neighbor = self.get_best(current_node)
            if(best_neighbor.total_cost > current_node.total_cost):
                current_node = best_neighbor
            else:
                return current_node

    def get_best(self, current_node, p):
        current_bset = current_node
        for action in p.get_actions:
            next_states = action.apply(current_node.state)
            for state in next_states:
                current_h = p.get_heuristic_function.getH(state)
                if(current_bset.get_total_cost() < current_h):
                    current_bset = Node(state)
                    current_bset.total_cost = current_h
        return current_bset