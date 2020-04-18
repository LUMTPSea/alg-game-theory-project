
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
        self.actions = {}
        self.state_space = []
        self.next_states = {}
        self.__fill_state_space()
        self.__fill_next_states_and_actions()
        self.__fill_transitions()
        self.__fill_rewards()

    def display(self):
        print("Dimensions: ({} x {})\n".format(self.rows, self.cols))

    def __fill_state_space(self):
        for r in range(1, self.rows):
            for c in range(1, self.cols):
                self.state_space.append(State(r, c))

    def __fill_transitions(self):
        pass

    def __fill_rewards(self):
        if self.rewards is None:
            for state in self.state_space:
                for action in self.actions.get(1, state):
                    triplet = 1, state, action
                    if state.x == 4 and state.y == 1 and action == 'E':
                        self.rewards[triplet] = -100
                    elif state.x == 4 and state.y == 12 and action == 'W':
                        self.rewards[triplet] = -100
                    elif state.x == 3 and state.y == 12 and action == 'S':
                        self.rewards[triplet] = 100
                    elif state.x == 3 and 2 <= state.y <= 11 and action == 'S':
                        self.rewards[triplet] = -100
                    else:
                        self.rewards[triplet] = -1

    def __is_valid(self, x, y):
        return 1 <= x <= self.rows and 1 <= y <= self.cols

    def __update_action_state(self, x, y, action, state):
        if self.__is_valid(x, y):
            self.actions[1, state].append(action)
            self.next_states[1, state].append(State(x, y))

    def __fill_next_states_and_actions(self):
        for state in self.state_space:
            nx, ny = state.x - 1, state.y
            ex, ey = state.x, state.y + 1
            wx, wy = state.x, state.y - 1
            sx, sy = state.x + 1, state.y

            self.next_states[1, state] = []
            self.actions[1, state] = []

            self.__update_action_state(nx, ny, 'N', state)
            self.__update_action_state(ex, ey, 'E', state)
            self.__update_action_state(wx, wy, 'W', state)
            self.__update_action_state(sx, sy, 'S', state)


    

