class IAction:
    def apply(self, state):
        pass

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, n):
        self.__name = n
