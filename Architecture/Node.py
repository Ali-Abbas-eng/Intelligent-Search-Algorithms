class Node:
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, c):
        self.__color = c

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, identification_number):
        self.__id = identification_number

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, s):
        self.__state = s

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, p):
        self.__parent = p

    @property
    def path_cost(self):
        return self.__path_cost

    @path_cost.setter
    def path_cost(self, pc):
        self.__path_cost = pc

    @property
    def total_cost(self):
        return self.__total_cost

    @total_cost.setter
    def total_cost(self, tc):
        self.__total_cost = tc

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, a):
        self.__action = a

    @property
    def depth(self):
        return self.__depth

    @depth.setter
    def depth(self, d):
        self.__depth = d

    @property
    def visiting_order(self):
        return self.__visiting_order

    @visiting_order.setter
    def visiting_order(self, vo):
        self.__visiting_order = vo

    def __init__(self, state, parent = None, action = None, path_cost = 0, total_cost = None):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        if(total_cost == None): self.total_cost = path_cost  # when the total cost is not provided treat path and total csots eaually
        else: self.total_cost = total_cost
        self.color = 'blue'
        self.visiting_order = -1
        if(not parent):
            self.path_cost = 0

    def is_root_node(self):
        return self.parent == None

    def get_path_from_root(self):
        current_node = self
        path = [current_node]
        while( not current_node.is_root_node() ):
            current_node = current_node.parent
            path.insert(0, current_node)
        return path

    def __str__(self):
        string = "Parent: "
        if(self.is_root_node()):
            string += "None (Initial State)"
        else:
            string += str(self.parent.state)
        string += "\nAction: "
        if(self.action == None):    string += "No Action"
        else:    string += self.action.name
        string += "\nPath Cost: " + str(self.path_cost)
        string += "\n" + str(self.state) + "\n"
        return string

    def equals(self, object):
        t = Node(object)
        return t.state.equals(self.state)

    def is_simialr_to(self, node):
        return(
            self.parent == node.parent and
            self.path_cost == node.path_cost and
            self.totoal_cost == node.totoal_cost and
            self.state.equals(node.state)
        )

    def __gt__(self, node):
        if(self. total_cost > node.total_cost):
            return 1
        elif(self.total_cost < node.total_cost):
            return -1
        return 0

