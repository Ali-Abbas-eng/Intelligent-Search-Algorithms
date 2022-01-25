from Game import Game
from IAction import IAction
from Player import Player
from State import State
from numpy import Inf

class MiniMaxSearch(Player):
    @property
    def game(self):
        return self.__game
    @game.setter
    def game(self, g):
        self.__game = g

    @property
    def is_max_player(self):
        return self.__is_max_player
    @is_max_player.setter
    def is_max_player(self, imp):
        self.__is_max_player = imp

    def __init__(self, game, is_max_player):
        self.is_max_player = is_max_player
        self.game = game

    def make_decision(self, state):
        result = None
        if(self.is_max_player):
            result_value = -Inf
            for action in self.game.get_actions(state):
                value = self.min_value(self.game.get_result(state = state, action = action))
                if(value > result_value):
                    result = action
                    result_value = value
        else:
            result_value = Inf
            for action in self.game.get_actions(state):
                value = self.max_value(self.game.get_result(state = state, action = action))
                if(value < result_value):
                    result = action
                    result_value = value
        return result

    def max_value(self,state):
        if(self.game.is_terminal(state)):
            return self.game.evaluate(state)
        value = -Inf
        for action in self.game.get_actions(state = state):
            value = max(value, self.min_value(self.game.get_result(state = state, action = action)))
        return value

    def min_value(self, state):
        if(self.game.is_terminal()):
            return self.game.evaluate(state)
        value = Inf
        for action in self.game.get_actions(state = state):
            value = min(value, self.game.get_result(state = state, action = action))
        return value
    