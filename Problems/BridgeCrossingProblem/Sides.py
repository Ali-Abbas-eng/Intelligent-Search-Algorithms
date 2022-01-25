from State import State


class Sides(State):
    @property
    def side1(self):
        return self.__side1
    @side1.setter
    def side1(self, s1):
        self.__side1 = s1

    @property
    def side2(self):
        return self.__side2
    @side2.setter
    def side2(self, s2):
        self.__side2 = s2

    def __init__(self, p1, p2, p3, lp):
        self.side1 = [p1, p2, p3, int(lp > 0)]
        self.side2 = [-p1, -p2, -p3, int(not lp) ]

    def __str__(self):
        return f"First Side: {self.side1}, Second Side: {self.side2}"

