class Game:

    @property
    def current_player(self):
        return self.__current_player

    @current_player.setter
    def current_player(self, c_player):
        self.__current_player = c_player


    def get_initial_state(self):
        pass

    def get_players(self):
        pass

    def get_player(self):
        pass

    def get_actions(self, state):
        pass

    def get_result(self, state, action):
        pass

    def is_terminal(self, state):
        pass

    def evaluate(self, state):
        pass

    def start_game(self):
        s = self.get_initial_state()

        while(not self.is_terminal(s)):
            print(s)
            p = self.get_player()
            a = p.make_decision(s)
            s = self.get_result(s,a)

        print(s)
        
