
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

    def lonr_v(self):
        for time in range(1, self.time_limit):
            for agent in range(1, self.num_agents):
                for state in self.state_space:
                    self.update_q(agent, state, time)

            for agent in range(1, self.num_agents):
                for state in self.state_space:
                    self.update_policy(agent, state, time)

    def update_q(self, agent, state, time):
        for action in self.actions.get(agent, state):
            action_val = 0
            for next_state in self.next_states.get(agent, state):
                trans_prob = self.transitions.get(agent, state, action, next_state)
                reward = self.rewards.get(agent, state, action)
                next_state_val = self.__get_next_state_value(agent, next_state, time)
                action_val += trans_prob * (reward + self.gamma * next_state_val)
            self.q[time + 1, agent, state, action] = action_val

    def __get_next_state_value(self, agent, next_state, time):
        val = 0
        for action in self.actions.get(agent, next_state):
            quartet = time, agent, next_state, action
            val += self.q[quartet] * self.pi[quartet]
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
        for action in self.actions.get(agent, state):
            immediate_regret = max(0, self.q[time + 1, agent, state, action] - expected_value)
            triplet = agent, state, action
            if triplet in self.regret_sums:
                self.regret_sums[triplet] += immediate_regret
            else:
                self.regret_sums[triplet] = immediate_regret

        for action in self.actions.get(agent, state):
            triplet = agent, state, action
            total_regret_sum += self.regret_sums[triplet]

        for action in self.actions.get(agent, state):
            triplet = agent, state, action
            if total_regret_sum > 0:
                self.pi[time + 1, triplet] = self.regret_sums[triplet] / total_regret_sum
            else:
                self.pi[time + 1, triplet] = 1 / len(self.actions.get(agent, state))
            if triplet in self.policy_sums:
                self.policy_sums[triplet] += self.pi[time + 1, triplet]
            else:
                self.policy_sums[triplet] = self.pi[time + 1, triplet]

    def __get_expected_reward(self, agent, state, time):
        val = 0
        for action in self.actions.get(agent, state):
            q_val = self.q[time + 1, agent, state, action]
            prob = self.pi[time, agent, state, action]
            val += prob * q_val
        return val

