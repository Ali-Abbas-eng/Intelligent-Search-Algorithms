from State import State

class WaterJugsState(State):
    @property
    def jugs(self):
        return self.__jugs
    @jugs.setter
    def jugs(self, j):
        self.__jugs = j

    def __init__(self, jugs):
        self.jugs = jugs

    def __str__(self):
        string = ""
        for jug in self.jugs:
            string += f"{jug[0]} "
        return string
