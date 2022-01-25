from HeuristicFunction import HeuristicFunction
from State import State

class SLDHeuristic(HeuristicFunction):
    @property
    def sld_map(self):
        return self.__sld_map
    @sld_map.setter
    def sld_map(self, sm):
        self.__sld_map = sm
    def __init__(self, sld_map):
        self.sld_map = sld_map

    def getH(self, state):
        return self.sld_map[state]