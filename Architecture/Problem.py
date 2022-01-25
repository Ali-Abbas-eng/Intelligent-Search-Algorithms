class Problem:
    @property
    def initial_state(self):
        return self.__initial_state
    @initial_state.setter
    def initial_state(self, state):
        self.__initial_state = state

    @property
    def goal_state(self):
        return self.__goal_state
    @goal_state.setter
    def goal_state(self, gs):
        self.__goal_state = gs

    @property
    def actions(self):
        return self.__actions
    @actions.setter
    def actions(self, actions):
        self.__actions = actions

    @property
    def action_cost(self):
        return self.__action_cost
    @action_cost.setter
    def action_cost(self, ac):
        self.__action_cost = ac
    def is_goal(self, state):
        pass

    def get_heuristic_function(self):
        pass

    def solv(self, search_algorithm):
        return search_algorithm.search(self)

