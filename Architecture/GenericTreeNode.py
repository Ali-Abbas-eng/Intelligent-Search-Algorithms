class GenericTreeNode:
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, v):
        self.__value = v

    @property
    def children(self):
        return self.__children
    @children.setter
    def children(self, c):
        self.__childre = c

    @property
    def parent(self):
        return self.__parent
    @parent.setter
    def parent(self, p):
        self.__parent = p

    def get_children_count(self):
        return len(self.children)

    def is_right_most_child(self):
        return (self.parent.children[self.parent.get_children_count() - 1].value.is_similar_to(self.value))

    def is_left_most_child(self):
        return (self.parent.children[0].value.is_similar_to(self.value))

    def __str__(self):
        return (str(self.value.state))