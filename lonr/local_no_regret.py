from environments.gridworld import GridWorld, State
import matplotlib.pyplot as plt


class LocalNoRegret:
    def __init__(self, time_limit, num_agents, state_space, actions, next_states, transitions, rewards, gamma):
        self.time_limit = time_limit
        self.num_agents = num_agents
        self.state_space = state_space
        self.actions = actions
        self.next_states = next_states
        self.transitions = transitions
        self.rewards = rewards
        self.gamma = gamma
        self.q, self.pi = {}, {}
        self.policy_sums = {}
        self.regret_sums = {}

    def __plot__val(self):
        # y_avg = [self.q[1, 1, State(4, 1), 'N']]
        y_abs = [self.q[1, 1, State(4, 1), 'N']]
        tot = 0
        for t in range(2, self.time_limit + 1):
            tot += self.q[t, 1, State(4, 1), 'N']
            y_abs.append(self.q[t, 1, State(4, 1), 'N'])
            # y_avg.append(tot / t)

        plt.plot([x for x in range(1, self.time_limit + 1)],
                 [-13.0 for _ in range(1, self.time_limit + 1)], linestyle=':')
        # plt.plot([x for x in range(1, self.time_limit + 1)], y_avg)
        plt.plot([x for x in range(1, self.time_limit + 1)], y_abs)
        plt.savefig('plot.png')

    def __display_q_values(self, time):
        for agent in range(1, self.num_agents + 1):
            print("For agent: ", agent)
            print("For time: ", time)
            for state in self.state_space:
                for action in self.actions[agent, state]:
                    print("For state: {}, action: {}, q_val: {}".format(
                        state, action, self.q[time, agent, state, action]))
                print()

    def __display_policy(self, time):
        for agent in range(1, self.num_agents + 1):
            print("For agent: ", agent)
            print("For time: ", time)
            for state in self.state_space:
                for action in self.actions[agent, state]:
                    print("For state: {}, action: {}, policy: {}".format(
                        state, action, self.pi[time, agent, state, action]))
                print()

    def lonr_v(self):
        for time in range(1, self.time_limit + 1):
            for agent in range(1, self.num_agents + 1):
                for state in self.state_space:
                    self.update_q(agent, state, time)
            # self.__display_q_values(time)

            for agent in range(1, self.num_agents + 1):
                for state in self.state_space:
                    self.update_policy(agent, state, time)

            # self.__display_policy(time)

        self.__plot__val()
        print(self.q[self.time_limit, 1, State(4, 1), 'N'])
        print(self.q[self.time_limit, 1, State(4, 1), 'E'])

    def update_q(self, agent, state, time):
        for action in self.actions[agent, state]:
            action_val = 0
            for next_state in self.next_states[agent, state]:
                trans_prob = self.transitions[agent, state, action, next_state]
                reward = self.rewards[agent, state, action]
                next_state_val = self.__get_next_state_value(agent, next_state, time)
                action_val += trans_prob * (reward + self.gamma * next_state_val)
            self.q[time, agent, state, action] = action_val

    def __get_next_state_value(self, agent, next_state, time):
        val = 0
        for action in self.actions[agent, next_state]:
            quartet = time - 1, agent, next_state, action
            q, pi = 0, 0
            if quartet in self.q:
                q = self.q[quartet]
            if (time - 1, agent, next_state, action) in self.pi:
                pi = self.pi[time - 1, agent, next_state, action]
            val += q * pi
        return val

    def update_policy(self, agent, state, time):
        """
        Using only RegretMatching++ here. Need
        to use other ones as well. Will abstract
        it out later.
        :param agent:
        :param state:
        :param time:
        :return:
        """
        expected_value, total_regret_sum = self.__get_expected_reward(agent, state, time), 0

        for action in self.actions[agent, state]:
            immediate_regret = max(0, self.q[time, agent, state, action] - expected_value)
            triplet = agent, state, action
            if triplet in self.regret_sums:
                self.regret_sums[triplet] += immediate_regret
            else:
                self.regret_sums[triplet] = immediate_regret

        for action in self.actions[agent, state]:
            triplet = agent, state, action
            total_regret_sum += self.regret_sums[triplet]

        for action in self.actions[agent, state]:
            triplet = agent, state, action
            if total_regret_sum > 0:
                self.pi[time, agent, state, action] = self.regret_sums[triplet] / total_regret_sum
            else:
                self.pi[time, agent, state, action] = 1 / len(self.actions[agent, state])
            if triplet in self.policy_sums:
                self.policy_sums[triplet] += self.pi[time, agent, state, action]
            else:
                self.policy_sums[triplet] = self.pi[time, agent, state, action]

    def __get_expected_reward(self, agent, state, time):
        val = 0
        for action in self.actions[agent, state]:
            q_val, prob = 0, 0
            if (time, agent, state, action) in self.q:
                q_val = self.q[time, agent, state, action]
            if (time - 1, agent, state, action) in self.pi:
                prob = self.pi[time - 1, agent, state, action]
            val += prob * q_val
        return val

