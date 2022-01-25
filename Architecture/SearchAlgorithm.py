from GenericTreeNode import GenericTreeNode


class SearchAlgorithm:
    @property
    def use_graph_search(self):
        return self.__use_graph_search
    @use_graph_search.setter
    def use_graph_search(self, ugs):
        self.__use_graph_search = ugs

    @property
    def developed_nodes(self):
        return self.__developed_nodes
    @developed_nodes.setter
    def developed_nodes(self, dn):
        self.__developed_nodes = dn

    @property
    def all_nodes(self):
        return self.__all_nodes
    @all_nodes.setter
    def all_nodes(self, an):
        self.__all_nodes = an

    @property
    def search_tree(self):
        return self.__search_tree
    @search_tree.setter
    def search_tree(self, st):
        self.__search_tree = st

    def __init__(self):
        self.all_nodes = []

    def search(self, problem):
        pass
    def get_node(self, node):
        if(len(self.all_nodes) == 0):
            return None
        i = 0
        n = self.all_nodes[i]
        while(not node.is_similar_to(n.value)):
            i += 1
            try:
                n = self.all_nodes[i]
            except Exception as ex:
                print(ex)
                return None

    def add_to_search_tree(self, parent, child):
        node = self.get_node(parent)
        tt = GenericTreeNode.GenericTreeNode()
        tt.value = child
        tt.parent = node
        node.children.append(tt)
        self.all_nodes.append(tt)

    def init_search_tree(self, node):
        self.search_tree.value = node
        self.search_tree.parent = None
        self.all_nodes.append(self.search_tree)

    def generate_search_tree(self):
        return self.generate_search_tree_string(self.search_tree, "", False, False, "")
    def generate_search_tree_string(self, node, prefix, is_right_most, is_left_most, string_builder = ""):
        half_size = (node.get_children_count() + 1) / 2
        children = node.children
        for i in range(len(children), half_size, -1):
            child = children[i]
            if(is_right_most and not is_left_most):
                s = "    "
            else:
                s = "|   "
            self.generate_search_tree_string(child, prefix + s, child.is_right_most_child(), child.is_left_most_child(), string_builder)

        if(is_right_most and is_left_most):
            x = "└── "
        else:
            x = ""

        if(is_right_most and not is_left_most):
            y = "┌── "
        else:
            y = ""

        if(not is_right_most and is_left_most):
            z = "└── "
        else:
            z = ""

        if(not is_left_most and not is_right_most):
            v = "├── "
        else:
            v = ""

        string_builder += (prefix + x + y + z + "[" + str(node.value.state) + ", g = " + node.value.path_cost + ", f = " + node.value.total_cost + ", vo = " + node.value.visiting_order + "]" + "\n")

        for i in range(half_size - 1, 0, -1):
            child = children[i]
            if(is_left_most):
                b = "    "
            else:
                b = "|   "
            self.generate_search_tree_string(child, prefix + b, child.is_right_most_child(), child.is_left_most_child, string_builder)

        return string_builder