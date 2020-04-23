
class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return int(str(hash(self.x)) + str(hash(self.y)))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)


class GridWorld:
    def __init__(self, rows=4, cols=12):
        self.rows = rows
        self.cols = cols
        self.transitions = {}
        self.rewards = {}
        self.actions = {}
        self.state_space = []
        self.next_states = {}
        self.__fill_state_space()
        self.__fill_next_states_and_actions()
        self.__fill_rewards()
        self.__fill_transitions()

    @classmethod
    def perform_action(cls, state, action):
        if action == 'N':
            return State(state.x - 1, state.y)
        elif action == 'E':
            return State(state.x, state.y + 1)
        elif action == 'W':
            return State(state.x, state.y - 1)
        else:
            return State(state.x + 1, state.y)

    def __display_rewards(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if r == self.rows - 1 and c == self.cols - 1:
                    continue
                print("State: ", r + 1, c + 1)
                tup = []
                for action in self.actions[1, State(r + 1, c + 1)]:
                    tup.append((action, self.rewards[1, State(r + 1, c + 1), action]))
                print(tup)
            print()

    def display(self):
        print("Grid Dimensions: ({} x {})\n".format(self.rows, self.cols))
        print("\n*States Space*: ", self.state_space)
        print("\n\n*Actions*: ", self.actions)
        self.__display_rewards()
        print("\n\n*Transitions*: ", self.transitions)

    def __fill_state_space(self):
        for r in range(1, self.rows + 1):
            for c in range(1, self.cols + 1):
                self.state_space.append(State(r, c))

    def __fill_transitions(self):
        for state in self.state_space:
            if state.x == self.rows and state.y == self.cols:
                continue
            nx, ny = state.x - 1, state.y
            ex, ey = state.x, state.y + 1
            wx, wy = state.x, state.y - 1
            sx, sy = state.x + 1, state.y
            if self.__is_valid(nx, ny):
                self.transitions[1, state, 'N', State(nx, ny)] = 1.0
                self.transitions[1, state, 'E', State(nx, ny)] = 0
                self.transitions[1, state, 'W', State(nx, ny)] = 0
                self.transitions[1, state, 'S', State(nx, ny)] = 0
            if self.__is_valid(ex, ey):
                self.transitions[1, state, 'N', State(ex, ey)] = 0
                self.transitions[1, state, 'E', State(ex, ey)] = 1.0
                self.transitions[1, state, 'W', State(ex, ey)] = 0
                self.transitions[1, state, 'S', State(ex, ey)] = 0
            if self.__is_valid(wx, wy):
                self.transitions[1, state, 'N', State(wx, wy)] = 0
                self.transitions[1, state, 'E', State(wx, wy)] = 0
                self.transitions[1, state, 'W', State(wx, wy)] = 1.0
                self.transitions[1, state, 'S', State(wx, wy)] = 0
            if self.__is_valid(sx, sy):
                self.transitions[1, state, 'N', State(sx, sy)] = 0
                self.transitions[1, state, 'E', State(sx, sy)] = 0
                self.transitions[1, state, 'W', State(sx, sy)] = 0
                self.transitions[1, state, 'S', State(sx, sy)] = 1.0

    def __fill_rewards(self):
        for state in self.state_space:
            for action in self.actions[1, state]:
                triplet = 1, state, action
                if state.x == 4 and state.y == 1 and action == 'E':
                    self.rewards[triplet] = -100
                elif state.x == 3 and 2 <= state.y <= 11 and action == 'S':
                    self.rewards[triplet] = -100
                elif (state.x == 4 and 3 <= state.y <= 10) and (action == 'E' or action == 'W'):
                    self.rewards[triplet] = -100
                elif state.x == 4 and state.y == 2 and action == 'W':
                    self.rewards[triplet] = -1
                elif state.x == 4 and state.y == 2 and action == 'E':
                    self.rewards[triplet] = -100
                elif state.x == 4 and state.y == 11 and action == 'W':
                    self.rewards[triplet] = -100
                elif state.x == 4 and state.y == 11 and action == 'E':
                    self.rewards[triplet] = -1
                elif state.x == 3 and state.y == 12 and action == 'S':
                    self.rewards[triplet] = -1
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

            if state.x == self.rows and state.y == self.cols:
                continue

            self.__update_action_state(nx, ny, 'N', state)
            self.__update_action_state(ex, ey, 'E', state)
            self.__update_action_state(wx, wy, 'W', state)
            self.__update_action_state(sx, sy, 'S', state)




