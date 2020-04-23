from environments.gridworld import GridWorld, State
from lonr.local_no_regret import LocalNoRegret

grid = GridWorld()
lonr = LocalNoRegret(time_limit=15000, num_agents=1, state_space=grid.state_space,
                     actions=grid.actions, next_states=grid.next_states, transitions=grid.transitions,
                     rewards=grid.rewards, gamma=1.0)
lonr.lonr_v()
