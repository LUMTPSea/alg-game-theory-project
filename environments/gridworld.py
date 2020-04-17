
class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GridWorld:
    def __init__(self, rows=4, cols=12, transitions=None, rewards=None):
        self.rows = rows
        self.cols = cols
        self.transitions = transitions
        self.rewards = rewards
        self.actions = ['up', 'down', 'right', 'left']
        self.state_space = []
        self.__fill_state_space()
        self.__fill_transitions()
        self.__fill_rewards()

    def display(self):
        print("Dimensions: ({} x {})\n".format(self.rows, self.cols))
        for r in range(1, self.rows):
            for c in range(1, self.cols):
                print(self.rewards.get(State(0, 0), State(r, c)), ' ')
            print("\n")

    def __fill_state_space(self):
        for r in range(1, self.rows):
            for c in range(1, self.cols):
                self.state_space.append(State(r, c))

    def __fill_transitions(self):
        if self.transitions is None:
            for r1 in range(self.rows):
                for c1 in range(self.cols):
                    for a in self.actions:

                        for r2 in range(self.rows):
                            for c2 in range(self.cols):
                                pass

    def __fill_rewards(self):
        if self.rewards is None:
            for r1 in range(self.rows):
                for c1 in range(self.cols):
                    for r2 in range(self.rows):
                        for c2 in range(self.cols):
                            state1, state2 = State(r1, c1), State(r2, c2)
                            pass
